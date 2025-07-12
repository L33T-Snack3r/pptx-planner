import os
from playwright.sync_api import sync_playwright

def check_slide_overflow(html_content, slide_width=1280, slide_height=720, enable_auto_adjust=True):
    """
    Checks for content overflow within a slide using a headless browser.
    Optionally attempts to auto-adjust font sizes if overflow is detected.

    Args:
        html_content (str): The full HTML string of the slide.
        slide_width (int): The target width of the slide in pixels.
        slide_height (int): The target height of the slide in pixels.
        enable_auto_adjust (bool): Whether to attempt font size reduction to fit content.

    Returns:
        dict: A dictionary containing:
            - 'status': 'no_overflow', 'resolved_overflow', 'critical_overflow', 'initial_overflow_detected', 'error'
            - 'message': A descriptive message.
            - 'overflow_details': Dictionary with scroll/client dimensions if applicable.
            - 'screenshot_path': Path to a generated screenshot for debugging (if overflow detected).
    """
    screenshot_path = None
    result = {
        'status': 'error',
        'message': 'An unexpected error occurred.',
        'overflow_details': {},
        'screenshot_path': None
    }

    with sync_playwright() as p:
        browser = None
        try:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.set_viewport_size({"width": slide_width, "height": slide_height})
            page.set_content(html_content)
            page.wait_for_load_state('networkidle')

            # --- MODIFIED JavaScript for overflow detection and optional auto-adjustment ---
            # The JavaScript function now accepts a single 'params' object
            js_function_string = """
            (function(params) { // Expecting a single 'params' object from Python
                const slideContent = document.querySelector('.slide-content');
                if (!slideContent) {
                    return { status: 'error', message: '.slide-content element not found.' };
                }

                // Destructure parameters for easier use
                const enableAutoAdjust = params.enableAutoAdjust;
                const minFontSize = params.minFontSize;
                const reductionFactor = params.reductionFactor;

                const elementsToAdjust = [
                    document.querySelector('.slide-title'),
                    ...slideContent.querySelectorAll('.section h3, .section p, .section ul, .section li')
                ].filter(Boolean);

                const checkForOverflow = () => {
                    const verticalOverflow = slideContent.scrollHeight > slideContent.clientHeight;
                    const horizontalOverflow = slideContent.scrollWidth > slideContent.clientWidth;
                    return verticalOverflow || horizontalOverflow;
                };

                let hasOverflow = checkForOverflow();
                let iterations = 0;
                const maxIterations = 20;

                if (!hasOverflow) {
                    return { status: 'no_overflow', message: 'No overflow detected.' };
                }

                let initialDimensions = {
                    scrollHeight: slideContent.scrollHeight,
                    clientHeight: slideContent.clientHeight,
                    scrollWidth: slideContent.scrollWidth,
                    clientWidth: slideContent.clientWidth
                };

                if (enableAutoAdjust && hasOverflow) {
                    while (hasOverflow && iterations < maxIterations) {
                        let madeChange = false;
                        elementsToAdjust.forEach(el => {
                            const currentSize = parseFloat(window.getComputedStyle(el).fontSize);
                            if (currentSize * reductionFactor >= minFontSize) {
                                el.style.fontSize = `${currentSize * reductionFactor}px`;
                                madeChange = true;
                            }
                        });

                        if (!madeChange && hasOverflow) {
                            break;
                        }
                        hasOverflow = checkForOverflow();
                        iterations++;
                    }

                    if (hasOverflow) {
                        return {
                            status: 'critical_overflow',
                            message: `Content still overflows after ${iterations} adjustments. Manual intervention needed.`,
                            overflow_details: {
                                initial: initialDimensions,
                                final: {
                                    scrollHeight: slideContent.scrollHeight,
                                    clientHeight: slideContent.clientHeight,
                                    scrollWidth: slideContent.scrollWidth,
                                    clientWidth: slideContent.clientWidth
                                }
                            }
                        };
                    } else {
                        return {
                            status: 'resolved_overflow',
                            message: `Overflow resolved by reducing font sizes in ${iterations} iterations.`,
                            overflow_details: {
                                initial: initialDimensions,
                                final: {
                                    scrollHeight: slideContent.scrollHeight,
                                    clientHeight: slideContent.clientHeight,
                                    scrollWidth: slideContent.scrollWidth,
                                    clientWidth: slideContent.clientWidth
                                }
                            }
                        };
                    }
                } else {
                    return {
                        status: 'initial_overflow_detected',
                        message: 'Overflow detected. Auto-adjustment is disabled or failed.',
                        overflow_details: {
                            initial: initialDimensions,
                            final: {
                                scrollHeight: slideContent.scrollHeight,
                                clientHeight: slideContent.clientHeight,
                                scrollWidth: slideContent.scrollWidth,
                                clientWidth: slideContent.clientWidth
                            }
                        }
                    };
                }
            })
            """
            # --- MODIFIED: Package arguments into a dictionary ---
            js_args = {
                'enableAutoAdjust': enable_auto_adjust,
                'minFontSize': 12, # Directly use numerical values here
                'reductionFactor': 0.98
            }
            # Pass the JavaScript function string and the single 'js_args' dictionary
            js_result = page.evaluate(js_function_string, js_args)
            result.update(js_result)

            # ... (rest of the check_slide_overflow function, unchanged) ...
            if result['status'] in ['initial_overflow_detected', 'critical_overflow', 'resolved_overflow']:
                screenshot_filename = f"slide_screenshot_{result['status']}.png"
                screenshot_path = os.path.join(os.getcwd(), screenshot_filename)
                page.screenshot(path=screenshot_path)
                result['screenshot_path'] = screenshot_path

        except Exception as e:
            result['status'] = 'error'
            result['message'] = f"Error during headless browser operation: {e}"
            print(f"Error: {e}")
        finally:
            if browser:
                browser.close()
    return result

# --- Your HTML Content (remains unchanged) ---
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Executive Summary - Intelligent Contract Document Search System</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
    <!-- Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        /* Base styles for the HTML document */
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: #f0f0f0;
            font-family: 'Roboto', sans-serif;
            overflow: hidden;
        }

        /* Styles for the main slide container */
        .slide-container {
            width: 1280px;
            height: 720px;
            background: linear-gradient(135deg, #1a2a3a 0%, #0a1a2a 100%);
            color: #e0e0e0;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 50px;
            box-sizing: border-box;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
            border-radius: 8px;
        }

        /* Styles for the main content area */
        .slide-content {
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            align-items: flex-start;
            text-align: left;
            width: 100%;
            padding-top: 0;
            overflow: hidden; /* CRITICAL: Ensures scrollHeight is accurate if content overflows */
        }

        /* Styles for the main slide title (e.g., "Executive Summary") */
        .slide-title {
            font-size: 2.2em;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 30px;
            line-height: 1.2;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            align-self: flex-start;
        }

        /* Container for the summary sections using a grid layout */
        .summary-sections {
            display: grid;
            grid-template-columns: auto auto;
            grid-template-rows: auto auto auto;
            gap: 30px;
            width: 100%;
            flex-grow: 1;
        }

        /* Styles for individual content sections (Problem, Solution, Benefits, CTA) */
        .section {
            background-color: rgba(255, 255, 255, 0.05);
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
        }

        /* Styles for section headings (e.g., "The Problem") */
        .section h3 {
            font-size: 1.6em;
            color: #ffffff;
            margin-top: 0;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
        }

        /* Styles for normal text within sections */
        .section p, .section ul {
            font-size: 1.2em;
            color: #e0e0e0;
            line-height: 1.4;
            margin-bottom: 0;
        }

        /* Specific grid placement for Problem and Solution */
        .section.problem {
            grid-column: 1 / 2;
            grid-row: 1 / 2;
        }

        .section.solution {
            grid-column: 2 / 3;
            grid-row: 1 / 2;
        }

        /* Specific grid placement for Key Benefits (spans both columns) */
        .section.benefits {
            grid-column: 1 / 3;
            grid-row: 2 / 3;
        }

        /* Styles for the benefits list */
        .section ul {
            list-style: none;
            padding-left: 0;
            margin-top: 8px;
        }

        .section ul li {
            margin-bottom: 8px;
            display: flex;
            align-items: flex-start;
        }

        /* Specific grid placement for Call to Action (spans both columns) */
        .section.call-to-action {
            grid-column: 1 / 3;
            grid-row: 3 / 4;
            text-align: center;
            background: linear-gradient(90deg, #007bff, #0056b3);
            color: #ffffff;
            padding: 25px;
            justify-content: center;
        }

        .call-to-action p {
            font-size: 1.3em;
            font-weight: 400;
        }

        /* Icon styling for section headings */
        .icon {
            margin-right: 10px;
            font-size: 1.1em;
            color: #007bff;
        }

        /* Icon styling for list items */
        .icon-small {
            margin-right: 8px;
            font-size: 0.9em;
            color: #28a745;
            flex-shrink: 0;
            padding-top: 2px;
        }

        /* Styles for the empty footer bar */
        .footer-bar {
            width: 100%;
            margin-top: auto;
            position: relative;
            height: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }

        /* Styles for the absolute positioned empty div within the footer */
        .footer-bar .absolute {
            position: absolute;
            bottom: 8px;
            right: 16px;
            color: #a0a0a0;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="slide-container">
        <div class="slide-content">
            <h1 class="slide-title">Executive Summary</h1>

            <div class="summary-sections">
                <div class="section problem">
                    <h3><i class="fas fa-exclamation-triangle icon"></i> The Problem</h3>
                    <p>Finding relevant contract documents is currently slow, inaccurate, and relies heavily on manual keyword searches, leading to missed information and potential risks. This process is time-consuming, error-prone, and can significantly hinder productivity and decision-making within the organization. This sentence is purposefully made very long to test the overflow detection capabilities of the system. Let's add even more text to ensure it definitely overflows and triggers the detection mechanism. This will help us verify that our headless browser setup correctly identifies content exceeding its designated boundaries. </p>
                </div>
                <div class="section solution">
                    <h3><i class="fas fa-lightbulb icon"></i> The Solution</h3>
                    <p>We propose an AI-powered semantic search system that understands the *meaning* of contracts and queries, delivering highly relevant results quickly. It will utilize natural language processing (NLP) and machine learning to go beyond simple keyword matching.</p>
                </div>
                <div class="section benefits">
                    <h3><i class="fas fa-star icon"></i> Key Benefits</h3>
                    <ul>
                        <li><i class="fas fa-check-circle icon-small"></i> Up to 90% Improvement in Search Accuracy</li>
                        <li><i class="fas fa-check-circle icon-small"></i> Reduce Contract Retrieval Time by 75%</li>
                        <li><i class="fas fa-check-circle icon-small"></i> Minimize Risk of Non-Compliance and Missed Obligations</li>
                        <li><i class="fas fa-check-circle icon-small"></i> Empower Employees with Faster Access to Critical Information</li>
                        <li><i class="fas fa-check-circle icon-small"></i> Enhance Overall Operational Efficiency</li>
                        <li><i class="fas fa-check-circle icon-small"></i> Facilitate Better Strategic Decision-Making</li>
                        <li><i class="fas fa-check-circle icon-small"></i> Improve Employee Satisfaction and Reduce Frustration</li>
                    </ul>
                </div>
                <div class="section call-to-action">
                    <h3><i class="fas fa-rocket icon"></i> Call to Action</h3>
                    <p>This proposal outlines a plan to transform contract document management, leading to significant cost savings, improved decision-making, and a stronger competitive advantage. Let's schedule a deep-dive to discuss implementation details and a tailored roadmap.</p>
                </div>
            </div>
        </div>

        <div class="footer-bar w-full mt-auto relative">
            <div class="absolute bottom-2 right-4 text-white text-sm"></div>
        </div>
    </div>
</body>
</html>
"""

# --- Example Usage for a standard Python script ---
if __name__ == "__main__":
    print("Checking slide for overflow (with auto-adjust enabled)...")
    result_with_adjust = check_slide_overflow(html_code, enable_auto_adjust=True)
    print("\n--- Result (with auto-adjust) ---")
    for key, value in result_with_adjust.items():
        print(f"{key}: {value}")

    print("\n-----------------------------------\n")

    print("Checking slide for overflow (with auto-adjust disabled)...")
    result_no_adjust = check_slide_overflow(html_code, enable_auto_adjust=False)
    print("\n--- Result (without auto-adjust) ---")
    for key, value in result_no_adjust.items():
        print(f"{key}: {value}")

    print("\n-----------------------------------\n")
    print("Check your current directory for generated screenshots (if any overflow detected).")