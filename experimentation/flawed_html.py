example_1 = \
{
"type" : "overflow",
"html" : \
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Our Solution: AI-Powered Semantic Search</title>
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
            min-height: 100vh; /* Ensures the slide is vertically centered on the page */
            background-color: #f0f0f0; /* Light background for the area outside the slide */
            font-family: 'Roboto', sans-serif; /* Modern, clean sans-serif font */
            overflow: hidden; /* Prevents scrollbars if the slide perfectly fits the viewport */
        }

        /* Styles for the main slide container */
        .slide-container {
            width: 1280px; /* 720p resolution width */
            height: 720px; /* 720p resolution height */
            background: linear-gradient(135deg, #1a2a3a 0%, #0a1a2a 100%); /* Deep navy/charcoal gradient for a professional, high-tech feel */
            color: #e0e0e0; /* Light gray for general text, ensuring good contrast */
            display: flex;
            flex-direction: column;
            justify-content: space-between; /* Distributes content and pushes footer to bottom */
            padding: 40px; /* Consistent padding */
            box-sizing: border-box; /* Includes padding in the width/height calculation */
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); /* Subtle shadow for depth and professionalism */
            border-radius: 8px; /* Slightly rounded corners for a modern touch */
        }

        /* Styles for the main content area */
        .slide-content {
            flex-grow: 1; /* Allows this section to take up available space */
            display: flex;
            flex-direction: column;
            justify-content: flex-start; /* Align content to the top */
            align-items: flex-start; /* Align content to the left */
            text-align: left; /* Default text alignment */
            width: 100%; /* Ensure it takes full width of padding area */
            padding-top: 0; /* Remove extra padding from title slide */
        }

        /* Styles for the main slide title */
        .slide-title {
            font-size: 2.3em; /* Specified title size */
            font-weight: 700; /* Bold for emphasis */
            color: #ffffff; /* Pure white for maximum impact */
            margin-bottom: 20px; /* Reduced from 30px to create more vertical space */
            line-height: 1.2;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* Subtle text shadow for depth */
            align-self: flex-start; /* Ensure it aligns to the start (left) */
        }

        /* Specific styles for this slide's content layout */
        .main-content-area {
            display: flex;
            flex-direction: column; /* Stack text description above comparison */
            align-items: center;
            width: 100%;
            flex-grow: 1; /* Take up remaining space */
            justify-content: center; /* Center content vertically */
        }

        .text-description {
            width: 80%; /* Constrain width for readability */
            margin-bottom: 20px; /* Reduced from 40px to create more vertical space */
            text-align: center; /* Center the descriptive text */
        }

        .intro-text {
            font-size: 1.3em; /* Larger text size as per instructions for short content */
            color: #e0e0e0;
            line-height: 1.6;
            margin-bottom: 10px; /* Reduced from 15px to create more vertical space */
            display: flex;
            align-items: flex-start; /* Align icon and text */
            justify-content: center; /* Center the text block */
            text-align: left; /* Ensure text within the flex item is left-aligned */
            padding-left: 20px; /* Indent for icon */
        }

        .intro-text i {
            margin-right: 15px;
            font-size: 1.5em; /* Larger icon for intro text */
            color: #007bff; /* Accent color */
            flex-shrink: 0;
        }

        .comparison-section {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 30px; /* Space between the search boxes and arrow */
            width: 100%;
        }

        .search-box {
            background-color: rgba(255, 255, 255, 0.08); /* Slightly lighter background for boxes */
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
            width: 400px; /* Fixed width for consistency */
            min-height: 360px; /* Increased from 280px to accommodate wrapped text and prevent cut-off */
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
        }

        .search-box h3 {
            font-size: 1.5em; /* Subtitle size for box titles */
            font-weight: 700;
            color: #ffffff;
            margin-top: 0;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
        }

        .search-box h3 i {
            margin-right: 10px;
            color: #007bff; /* Accent color for box titles */
        }

        .query-input {
            background-color: rgba(0, 0, 0, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 10px 15px;
            border-radius: 5px;
            margin-bottom: 20px;
            font-size: 1.1em;
            color: #b0c4de;
            font-style: italic;
        }

        .results {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .results li {
            font-size: 1.1em; /* Normal text size for results */
            color: #e0e0e0;
            margin-bottom: 10px;
            display: flex;
            align-items: flex-start;
        }

        .results li i {
            margin-right: 10px;
            font-size: 1.2em;
            flex-shrink: 0;
            padding-top: 2px; /* Align icon with text baseline */
        }

        .relevant-icon {
            color: #28a745; /* Green for relevant results */
        }

        .irrelevant-icon {
            color: #dc3545; /* Red for irrelevant results */
        }

        .arrow-icon {
            font-size: 3em; /* Large arrow icon */
            color: #007bff; /* Accent color for arrow */
            animation: bounceArrow 2s infinite; /* Subtle animation */
        }

        @keyframes bounceArrow {
            0%, 100% { transform: translateX(0); }
            50% { transform: translateX(10px); }
        }

        /* Styles for the empty footer bar */
        .footer-bar {
            width: 100%;
            margin-top: auto; /* Pushes the footer to the very bottom */
            position: relative;
            height: 20px; /* Defines the height of the footer area */
            border-top: 1px solid rgba(255, 255, 255, 0.1); /* A subtle separator line */
        }

        /* Styles for the absolute positioned empty div within the footer */
        .footer-bar .absolute {
            position: absolute;
            bottom: 8px; /* Positioned from the bottom of its relative parent */
            right: 16px; /* Positioned from the right of its relative parent */
            color: #a0a0a0; /* Matches other info text color */
            font-size: 0.9em; /* Slightly smaller font size */
        }
    </style>
</head>
<body>
    <div class="slide-container">
        <div class="slide-content">
            <h1 class="slide-title">Our Solution: AI-Powered Semantic Search</h1>

            <div class="main-content-area">
                <div class="text-description">
                    <p class="intro-text"><i class="fas fa-brain"></i> Semantic search understands the <em>meaning</em> and <em>intent</em> behind your queries, not just matching keywords.</p>
                    <p class="intro-text"><i class="fas fa-cogs"></i> It leverages cutting-edge AI technologies, including Transformer models, to analyze the context and relationships within contract documents.</p>
                    <p class="intro-text"><i class="fas fa-search-plus"></i> This allows for more accurate and relevant search results, even when using synonyms, paraphrases, or complex legal terminology.</p>
                </div>

                <div class="comparison-section">
                    <div class="search-box keyword-search">
                        <h3><i class="fas fa-keyboard"></i> Keyword Search</h3>
                        <div class="query-input">Query: "Termination Clause"</div>
                        <ul class="results">
                            <li><i class="fas fa-times-circle irrelevant-icon"></i> Document A: "Termination Clause 1.1" (Irrelevant context)</li>
                            <li><i class="fas fa-check-circle relevant-icon"></i> Document B: "Termination Clause 2.3" (Relevant)</li>
                            <li><i class="fas fa-times-circle irrelevant-icon"></i> Document C: "Project Termination Clause" (Irrelevant project)</li>
                            <li><i class="fas fa-times-circle irrelevant-icon"></i> Document D: "Early Termination Clause" (Relevant, but misses others)</li>
                        </ul>
                    </div>

                    <div class="arrow-icon"><i class="fas fa-arrow-right"></i></div>

                    <div class="search-box semantic-search">
                        <h3><i class="fas fa-lightbulb"></i> Semantic Search</h3>
                        <div class="query-input">Query: "Termination Clause"</div>
                        <ul class="results">
                            <li><i class="fas fa-check-circle relevant-icon"></i> Document B: "Termination Clause 2.3" (Relevant)</li>
                            <li><i class="fas fa-check-circle relevant-icon"></i> Document E: "Contract End Provisions" (Relevant - synonym)</li>
                            <li><i class="fas fa-check-circle relevant-icon"></i> Document F: "Cancellation Policy" (Relevant - paraphrase)</li>
                            <li><i class="fas fa-check-circle relevant-icon"></i> Document G: "Expiration Terms" (Relevant - related concept)</li>
                        </ul>
                    </div>
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
}

example_2 = \
{
"type" : "overflow",
"html" : \
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Executive Summary - Intelligent Contract Document Search</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        /* Define CSS Variables for easy theme management */
        :root {
            --primary-dark-blue: #1C3A5E; /* Deep corporate blue */
            --secondary-blue: #3A6B9C; /* Lighter, vibrant blue/teal */
            --text-light: #F0F0F0; /* Off-white for main text */
            --text-subtle: #C0C0C0; /* Lighter grey for subtitles */
            --text-footer: #A0A0A0; /* Even lighter grey for footer info */
            --logo-placeholder-bg: rgba(255, 255, 255, 0.08); /* Subtle transparent white for logos */
            --footer-bar-bg: rgba(0, 0, 0, 0.2); /* Semi-transparent dark for footer bar */
            --box-bg: rgba(255, 255, 255, 0.08); /* Background for content boxes */
            --highlight-color: #7ED957; /* A vibrant green for highlights, contrasting with blue */
        }

        /* Basic reset and body styling */
        body {
            margin: 0;
            padding: 0;
            font-family: 'Montserrat', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh; /* Ensures the slide is centered vertically on the page */
            background-color: #000; /* Fallback background for outside the slide */
        }

        /* Slide Container - Defines the 720p slide dimensions and overall layout */
        .slide-container {
            width: 1280px; /* 720p width */
            height: 720px; /* 720p height */
            display: flex;
            flex-direction: column;
            justify-content: space-between; /* Distributes content top, middle, bottom */
            /* align-items: center; Removed to allow left alignment of title */
            background: linear-gradient(135deg, var(--primary-dark-blue) 0%, var(--secondary-blue) 100%); /* Corporate blue/green gradient */
            color: var(--text-light);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3); /* Subtle shadow for depth */
            overflow: hidden; /* Prevents content from spilling out */
            position: relative; /* For any absolutely positioned elements within */
            padding: 0 60px; /* Global horizontal padding for content */
            box-sizing: border-box; /* Include padding in width calculation */
        }

        /* Header Logos Section (from Title Slide - kept for consistency but not used on this slide) */
        .header-logos {
            display: flex;
            justify-content: space-between;
            width: 100%;
            padding: 30px 60px 0; /* Top and side padding */
            box-sizing: border-box; /* Include padding in width calculation */
            z-index: 10; /* Ensures logos are on top of other elements */
            display: none; /* Hide on this slide */
        }

        .logo {
            width: 150px;
            height: 50px;
            background-color: var(--logo-placeholder-bg);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.8em;
            color: rgba(255, 255, 255, 0.4);
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: 600;
        }

        /* Main Content Area (from Title Slide - modified for this slide's layout) */
        .main-content {
            text-align: center;
            max-width: 900px; /* Limits content width for readability */
            padding: 0 80px;
            flex-grow: 1; /* Allows it to take up available vertical space */
            display: flex;
            flex-direction: column;
            justify-content: center; /* Centers content vertically within this flex item */
            align-items: center;
            z-index: 5;
            display: none; /* Hide on this slide */
        }

        /* Graphic Icon Styling (from Title Slide - not used on this slide) */
        .graphic {
            width: 160px;
            height: 160px;
            margin-bottom: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            display: none; /* Hide on this slide */
        }

        .graphic svg {
            width: 100%;
            height: 100%;
            fill: var(--text-light); /* Icon color inherits from text */
            opacity: 0.8; /* Slightly transparent for subtlety */
        }

        /* Title Styling (from Title Slide - not used for main slide title on this slide) */
        .title {
            font-size: 3.0em; /* As per request */
            font-weight: 700; /* Bold for impact */
            margin-bottom: 20px;
            line-height: 1.25; /* Improves readability of multi-line titles */
            color: var(--text-light);
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* Subtle text shadow */
            display: none; /* Hide on this slide */
        }

        /* Subtitle Styling (from Title Slide - not used on this slide) */
        .subtitle {
            font-size: 1.8em; /* As per request */
            font-weight: 400; /* Lighter weight for contrast */
            color: var(--text-subtle);
            line-height: 1.4;
            max-width: 700px; /* Limits subtitle width */
            display: none; /* Hide on this slide */
        }

        /* Footer Information (Presented by, Date - from Title Slide - not used on this slide) */
        .footer-info {
            text-align: center;
            margin-bottom: 30px;
            font-size: 0.95em;
            color: var(--text-footer);
            z-index: 10;
            display: none; /* Hide on this slide */
        }

        .footer-info p {
            margin: 5px 0; /* Spacing between lines */
        }

        /* Slide Title (e.g., "Executive Summary") */
        .slide-title {
            font-size: 2.3em;
            font-weight: 700;
            color: var(--text-light);
            margin-top: 40px; /* Space from top */
            margin-bottom: 0; /* No bottom margin, content-area handles spacing */
            text-align: left;
            width: 100%; /* Ensures it takes full width within padding */
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }

        /* Main Content Area for the grid */
        .content-area {
            flex-grow: 1; /* Allows it to take up available vertical space */
            display: flex;
            align-items: center; /* Centers the grid vertically within this area */
            justify-content: center; /* Centers the grid horizontally */
            width: 100%;
            padding-top: 40px; /* Space between title and grid */
            padding-bottom: 40px; /* Space between grid and footer */
            box-sizing: border-box;
        }

        /* Content Grid Layout */
        .content-grid {
            display: grid;
            grid-template-columns: 1fr 1fr; /* Two equal columns */
            grid-template-rows: auto auto; /* Rows adjust to content */
            gap: 40px; /* Space between grid items */
            width: 100%; /* Takes full width of content-area */
            max-width: 1160px; /* 1280px - 2*60px padding */
        }

        /* Individual Content Boxes */
        .content-box {
            background-color: var(--box-bg);
            border-radius: 12px;
            padding: 30px;
            display: flex;
            flex-direction: column;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15); /* Subtle shadow for boxes */
            transition: transform 0.2s ease-in-out; /* Hover effect */
        }

        .content-box:hover {
            transform: translateY(-5px); /* Slight lift on hover */
        }

        /* Section Titles within boxes (Problem, Solution, etc.) */
        .section-title {
            font-size: 1.3em;
            font-weight: 600;
            margin-bottom: 20px;
            color: var(--text-light);
            display: flex;
            align-items: center;
            line-height: 1.2;
        }

        /* Icons next to section titles */
        .section-title .icon {
            width: 28px;
            height: 28px;
            min-width: 28px; /* Prevent shrinking */
            margin-right: 12px;
            fill: var(--highlight-color); /* Use highlight color for section icons */
            opacity: 0.9;
        }

        /* Bullet List Styling */
        .bullet-list {
            list-style: none;
            padding: 0;
            margin: 0;
            flex-grow: 1; /* Allows list to take available space in box */
        }

        /* Individual Bullet Points */
        .bullet-point {
            display: flex;
            align-items: flex-start; /* Align icon and text at the top */
            margin-bottom: 15px;
            line-height: 1.5;
            font-size: 0.9em;
            color: var(--text-subtle); /* Slightly lighter text for bullet points */
        }

        .bullet-point:last-child {
            margin-bottom: 0; /* No margin for the last bullet point */
        }

        /* Icons next to bullet points */
        .bullet-point .icon {
            width: 20px;
            height: 20px;
            min-width: 20px; /* Prevent shrinking */
            margin-right: 10px;
            margin-top: 2px; /* Adjust vertical alignment with text */
            fill: var(--secondary-blue); /* Use secondary blue for bullet icons */
            opacity: 0.8;
        }

        /* Highlighted text within bullet points */
        .highlight {
            font-weight: 700;
            color: var(--highlight-color); /* Use the new highlight color */
        }

        /* Empty Footer Bar - Template Master Slide Element */
        .footer-bar {
            width: 100%;
            height: 25px; /* Height of the bar */
            background-color: var(--footer-bar-bg);
            position: relative; /* Required for absolute positioning of child */
            z-index: 10;
            margin-top: auto; /* Pushes it to the bottom */
            /* Adjust width to span full 1280px, counteracting slide-container's padding */
            margin-left: -60px;
            margin-right: -60px;
            width: calc(100% + 120px);
        }

        /* Empty Div inside Footer Bar - For future page numbers/branding */
        .footer-bar .absolute {
            position: absolute;
            bottom: 8px; /* Interpreted from 'bottom-2' */
            right: 16px; /* Interpreted from 'right-4' */
            color: var(--text-light);
            font-size: 0.8em; /* Interpreted from 'text-sm' */
            opacity: 0.7;
        }
    </style>
</head>
<body>
    <div class="slide-container">
        <h1 class="slide-title">Executive Summary</h1>

        <div class="content-area">
            <div class="content-grid">
                <!-- Problem Section -->
                <div class="content-box">
                    <h3 class="section-title">
                        <svg class="icon" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z"/>
                        </svg>
                        Problem
                    </h3>
                    <ul class="bullet-list">
                        <li class="bullet-point">
                            <svg class="icon" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9h1.5v9H10zm3.5 0v-9H15v9h-1.5z"/>
                            </svg>
                            Current keyword-based search methods are inefficient and inadequate for navigating vast, complex, and unstructured internal contract documents.
                        </li>
                        <li class="bullet-point">
                            <svg class="icon" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9h1.5v9H10zm3.5 0v-9H15v9h-1.5z"/>
                            </svg>
                            This leads to: missed critical information, significant time waste in legal review and business operations, and potential compliance risks.
                        </li>
                    </ul>
                </div>

                <!-- Solution Section -->
                <div class="content-box">
                    <h3 class="section-title">
                        <svg class="icon" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M9 21c0 .55.45 1 1 1h4c.55 0 1-.45 1-1v-1H9v1zm3-19C8.14 2 5 5.14 5 9c0 2.38 1.19 4.47 3 5.74V17h8v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.86-3.14-7-7-7z"/>
                        </svg>
                        Solution
                    </h3>
                    <ul class="bullet-list">
                        <li class="bullet-point">
                            <svg class="icon" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9h1.5v9H10zm3.5 0v-9H15v9h-1.5z"/>
                            </svg>
                            We propose building a cutting-edge AI-powered Semantic Search system.
                        </li>
                        <li class="bullet-point">
                            <svg class="icon" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9h1.5v9H10zm3.5 0v-9H15v9h-1.5z"/>
                            </svg>
                            This system leverages the <span class="highlight">Retrieval Augmented Generation (RAG)</span> architecture, powered by <span class="highlight">Large Language Models (LLMs)</span> and specialized <span class="highlight">Vector Databases</span>.
                        </li>
                    </ul>
                </div>

                <!-- Key Benefits Section -->
                <div class="content-box">
                    <h3 class="section-title">
                        <svg class="icon" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/>
                        </svg>
                        Key Benefits
                    </h3>
                    <ul class="bullet-list">
                        <li class="bullet-point">
                            <svg class="icon" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9h1.5v9H10zm3.5 0v-9H15v9h-1.5z"/>
                            </svg>
                            <span class="highlight">Enhanced Accuracy:</span> Understands meaning and context, not just keywords.
                        </li>
                        <li class="bullet-point">
                            <svg class="icon" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9h1.5v9H10zm3.5 0v-9H15v9h-1.5z"/>
                            </svg>
                            <span class="highlight">Semantic Understanding:</span> Finds truly relevant information, even if exact terms aren't present.
                        </li>
                        <li class="bullet-point">
                            <svg class="icon" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9h1.5v9H10zm3.5 0v-9H15v9h-1.5z"/>
                            </svg>
                            <span class="highlight">Rapid Information Retrieval:</span> Instantly access precise answers from your document corpus.
                        </li>
                        <li class="bullet-point">
                            <svg class="icon" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9h1.5v9H10zm3.5 0v-9H15v9h-1.5z"/>
                            </svg>
                            <span class="highlight">Reduced "Hallucinations":</span> Answers are strictly grounded in your internal data, ensuring factual accuracy.
                        </li>
                        <li class="bullet-point">
                            <svg class="icon" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9h1.5v9H10zm3.5 0v-9H15v9h-1.5z"/>
                            </svg>
                            <span class="highlight">Future-Proof Scalability:</span> Designed to grow with your document volume and evolve with AI advancements.
                        </li>
                        <li class="bullet-point">
                            <svg class="icon" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9h1.5v9H10zm3.5 0v-9H15v9h-1.5z"/>
                            </svg>
                            <span class="highlight">Robust Security:</span> Your proprietary data remains secure and private.
                        </li>
                    </ul>
                </div>

                <!-- Outcome Section -->
                <div class="content-box">
                    <h3 class="section-title">
                        <svg class="icon" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M16 6l2.29 2.29-4.88 4.88-4-4L2 16.59 3.41 18l6-6 4 4 6.3-6.29L22 12V6z"/>
                        </svg>
                        Outcome
                    </h3>
                    <ul class="bullet-list">
                        <li class="bullet-point">
                            <svg class="icon" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9h1.5v9H10zm3.5 0v-9H15v9h-1.5z"/>
                            </svg>
                            Transform how your legal, sales, and business teams interact with contract data.
                        </li>
                        <li class="bullet-point">
                            <svg class="icon" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9h1.5v9H10zm3.5 0v-9H15v9h-1.5z"/>
                            </svg>
                            Boost productivity, improve decision-making, and significantly strengthen compliance posture.
                        </li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="footer-bar">
            <div class="absolute"></div>
        </div>
    </div>
</body>
</html>
"""
}

example_3 = \
{
"type" : "overflow",
"html" : \
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Problem: The Business Impact - Intelligent Contract Document Search System</title>
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        /* General Body Styles */
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh; /* Ensure it takes full viewport height for centering */
            background-color: #f0f0f0; /* Light background for the page itself */
            font-family: 'Lato', sans-serif; /* Primary font */
            color: #ffffff; /* Default text color for the slide */
            overflow: hidden; /* Prevent scrollbars if slide is larger than viewport */
        }

        /* Slide Container - Defines 720p resolution */
        .slide {
            width: 1280px; /* 720p width */
            height: 720px; /* 720p height */
            background: linear-gradient(135deg, #1a2a3a 0%, #0f1a25 100%); /* Dark blue/grey gradient */
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); /* Subtle shadow for depth */
            display: flex;
            flex-direction: column;
            padding: 60px 80px; /* Internal padding for content */
            box-sizing: border-box; /* Include padding in width/height */
            position: relative; /* Crucial for absolute positioning of logo and footer */
            overflow: hidden; /* Ensure nothing spills out */
        }

        /* Main Content Area */
        .content-area {
            flex-grow: 1; /* Allows content to take available space */
            display: flex;
            flex-direction: column; /* Stack title and grid vertically */
            justify-content: flex-start; /* Align content to the top */
            align-items: flex-start; /* Align text to the left */
            text-align: left;
            padding-bottom: 0; /* No presenter info, so no need for bottom padding here */
            z-index: 1; /* Below logo */
        }

        /* Slide Title Styling (for all slides after title slide) */
        .slide-title {
            font-family: 'Roboto', sans-serif;
            font-size: 2.3em; /* Specified size */
            font-weight: 700;
            color: #e0e0e0;
            margin: 0 0 40px 0; /* Space below title */
            width: 100%; /* Ensure it takes full width */
        }

        /* Content Grid for Problem Slide */
        .problem-content-grid {
            display: grid;
            grid-template-columns: 1fr 1fr; /* Two columns, left for text, right for visual */
            gap: 60px; /* Gap between columns */
            width: 100%;
            flex-grow: 1; /* Allow grid to take remaining space */
            align-items: center; /* Vertically center content in grid cells */
        }

        .text-section {
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .visual-section {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%; /* Take full height of grid cell */
        }

        /* Section Heading Styling */
        .section-heading {
            font-family: 'Roboto', sans-serif;
            font-size: 1.8em; /* Subtitle size, increased for short content */
            font-weight: 700;
            color: #e0e0e0;
            margin: 0 0 20px 0;
            display: flex;
            align-items: center;
        }

        /* Icon Styling for Headings */
        .section-heading .icon {
            font-size: 1.5em; /* Larger icon for headings */
            margin-right: 15px;
            color: #ffcc00; /* Yellow for problem/impact */
        }

        /* Bullet List Styling */
        .bullet-list {
            list-style: none;
            padding: 0;
            margin: 0 0 40px 0; /* Space below list */
            width: 100%;
        }

        .bullet-list li {
            font-size: 1.3em; /* Normal text size, increased for short sentences */
            font-weight: 300;
            line-height: 1.5;
            color: #b0c4de;
            margin-bottom: 15px;
            display: flex;
            align-items: flex-start;
        }

        .bullet-list li:last-child {
            margin-bottom: 0;
        }

        /* Icon Styling for List Items */
        .bullet-list .list-icon {
            font-size: 1.2em;
            margin-right: 15px;
            color: #ff6347; /* Tomato red for impact/risk */
            flex-shrink: 0; /* Prevent icon from shrinking */
            padding-top: 2px; /* Align icon with text baseline */
        }

        /* Strategic Goals List Styling */
        .strategic-goals-list {
            list-style: none;
            padding: 0;
            margin: 0;
            width: 100%;
        }

        .strategic-goals-list li {
            font-size: 1.3em; /* Normal text size, increased for short sentences */
            font-weight: 300;
            line-height: 1.5;
            color: #b0c4de;
            margin-bottom: 15px;
            display: flex;
            align-items: flex-start;
        }

        .strategic-goals-list li:last-child {
            margin-bottom: 0;
        }

        .strategic-goals-list .list-icon {
            font-size: 1.2em;
            margin-right: 15px;
            color: #66b3ff; /* Blue for strategic goals */
            flex-shrink: 0;
            padding-top: 2px;
        }

        /* Bar Graph Styling */
        .bar-graph-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-end; /* Align bars to the bottom */
            width: 100%;
            height: 400px; /* Fixed height for the graph area */
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 20px;
            box-sizing: border-box;
            position: relative; /* For Y-axis label */
        }

        .graph-title {
            font-family: 'Roboto', sans-serif;
            font-size: 1.5em;
            font-weight: 700;
            color: #e0e0e0;
            margin-bottom: 20px;
            text-align: center;
            width: 100%;
        }

        .y-axis-label {
            position: absolute;
            left: 10px;
            top: 50%;
            transform: translateY(-50%) rotate(-90deg);
            font-size: 1em;
            color: #b0c4de;
            white-space: nowrap;
        }

        .bars-wrapper {
            display: flex;
            align-items: flex-end; /* Align bars to the bottom */
            gap: 80px; /* Space between bars */
            height: 100%; /* Take full height of container */
            padding-bottom: 20px; /* Space for X-axis labels */
        }

        .bar-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 120px; /* Width of each bar */
        }

        .bar {
            width: 100%;
            background-color: #66b3ff; /* Default bar color */
            border-radius: 5px 5px 0 0;
            transition: height 0.5s ease-out; /* Smooth transition for height change */
            position: relative;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            padding-top: 10px;
            box-sizing: border-box;
        }

        .bar.current {
            height: 250px; /* Represents 20 hours */
            background-color: #ff6347; /* Red for current/problem */
        }

        .bar.projected {
            height: 62.5px; /* Represents 5 hours (20 * 0.25) */
            background-color: #4CAF50; /* Green for projected/solution */
        }

        .bar-value {
            color: #ffffff;
            font-size: 1.1em;
            font-weight: 700;
            margin-top: -30px; /* Position value above the bar */
            text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
        }

        .bar-label {
            margin-top: 15px;
            font-size: 1.1em;
            color: #b0c4de;
            font-weight: 400;
        }

        /* Footer Bar */
        .footer-bar {
            width: 100%;
            height: 40px; /* Height of the footer bar */
            background-color: rgba(0, 0, 0, 0.2); /* Semi-transparent dark bar */
            position: absolute; /* Position relative to .slide */
            bottom: 0; /* Stick to the bottom of the slide */
            left: 0;
            display: flex;
            align-items: center;
            justify-content: flex-end; /* Push content to the right */
            padding-right: 40px; /* Padding for the right-aligned text */
            box-sizing: border-box;
            z-index: 10; /* Ensure it's on top */
        }

        /* Empty Footer Content (as per request) */
        .footer-bar .absolute {
            position: absolute; /* Position relative to .footer-bar */
            bottom: 8px; /* Equivalent to Tailwind's bottom-2 (approx 8px) */
            right: 16px; /* Equivalent to Tailwind's right-4 (approx 16px) */
            color: white;
            font-size: 0.875em; /* Equivalent to Tailwind's text-sm (approx 14px) */
        }
    </style>
</head>
<body>
    <div class="slide">
        <div class="content-area">
            <h1 class="slide-title">The Problem: The Business Impact</h1>

            <div class="problem-content-grid">
                <div class="text-section">
                    <h2 class="section-heading"><i class="fas fa-chart-line icon"></i> Quantifiable Impact</h2>
                    <ul class="bullet-list">
                        <li><i class="fas fa-hourglass-half list-icon"></i> Estimated 20 hours/week spent by legal team searching for specific contract clauses.</li>
                        <li><i class="fas fa-hand-holding-usd list-icon"></i> Potential 15% reduction in legal review time, freeing up resources for strategic initiatives.</li>
                        <li><i class="fas fa-exclamation-circle list-icon"></i> Risk of $500,000 in potential penalties due to missed contract renewal dates.</li>
                    </ul>

                    <h2 class="section-heading"><i class="fas fa-bullseye icon"></i> Connection to Strategic Goals</h2>
                    <ul class="strategic-goals-list">
                        <li><i class="fas fa-check-circle list-icon"></i> Faster deal closure by providing quick access to relevant contract terms.</li>
                        <li><i class="fas fa-shield-alt list-icon"></i> Better risk management through comprehensive identification of contractual obligations.</li>
                        <li><i class="fas fa-balance-scale list-icon"></i> Improved compliance with regulatory requirements by ensuring all relevant clauses are identified.</li>
                    </ul>
                </div>

                <div class="visual-section">
                    <div class="bar-graph-container">
                        <h3 class="graph-title">Contract Retrieval Time Comparison</h3>
                        <div class="y-axis-label">Time (Hours/Week)</div>
                        <div class="bars-wrapper">
                            <div class="bar-item">
                                <div class="bar current">
                                    <span class="bar-value">20 hrs</span>
                                </div>
                                <span class="bar-label">Current Retrieval</span>
                            </div>
                            <div class="bar-item">
                                <div class="bar projected">
                                    <span class="bar-value">~5 hrs</span>
                                </div>
                                <span class="bar-label">Projected with AI</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="footer-bar">
            <div class="absolute bottom-2 right-4 text-white text-sm"></div>
        </div>
    </div>
</body>
</html>
"""
}

example_4 = \
{
"type" : "overflow",
"html" : \
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Technology Stack - Intelligent Contract Document Search System</title>
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        /* General Body Styles */
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh; /* Ensure it takes full viewport height for centering */
            background-color: #f0f0f0; /* Light background for the page itself */
            font-family: 'Lato', sans-serif; /* Primary font */
            color: #ffffff; /* Default text color for the slide */
            overflow: hidden; /* Prevent scrollbars if slide is larger than viewport */
        }

        /* Slide Container - Defines 720p resolution */
        .slide {
            width: 1280px; /* 720p width */
            height: 720px; /* 720p height */
            background: linear-gradient(135deg, #1a2a3a 0%, #0f1a25 100%); /* Dark blue/grey gradient */
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); /* Subtle shadow for depth */
            display: flex;
            flex-direction: column;
            padding: 60px 80px; /* Internal padding for content */
            box-sizing: border-box; /* Include padding in width/height */
            position: relative; /* Crucial for absolute positioning of logo and footer */
            overflow: hidden; /* Ensure nothing spills out */
        }

        /* Main Content Area */
        .content-area {
            flex-grow: 1; /* Allows content to take available space */
            display: flex;
            flex-direction: column; /* Stack title and grid vertically */
            justify-content: flex-start; /* Align content to the top */
            align-items: flex-start; /* Align text to the left */
            text-align: left;
            padding-bottom: 0; /* No presenter info, so no need for bottom padding here */
            z-index: 1; /* Below logo */
        }

        /* Slide Title Styling (for all slides after title slide) */
        .slide-title {
            font-family: 'Roboto', sans-serif;
            font-size: 2.3em; /* Specified size */
            font-weight: 700;
            color: #e0e0e0;
            margin: 0 0 40px 0; /* Space below title */
            width: 100%; /* Ensure it takes full width */
        }

        /* Technology Stack Grid Layout */
        .tech-stack-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr); /* Two equal columns */
            gap: 40px 60px; /* Vertical and horizontal gap */
            width: 100%; /* Take full width of content area */
            flex-grow: 1; /* Allow grid to take remaining space */
            align-items: start; /* Align items to the start of their grid area */
        }

        /* Individual Technology Card Styling */
        .tech-card {
            background-color: rgba(255, 255, 255, 0.07); /* Slightly lighter background for sections */
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            height: 100%; /* Ensure cards in a row have similar height if content varies */
        }

        /* Icon Styling for Tech Cards */
        .tech-card .icon {
            font-size: 2.5em; /* Larger icon for emphasis */
            margin-bottom: 15px;
            color: #66b3ff; /* Bright blue for icons */
        }

        /* Technology Name Styling */
        .tech-name {
            font-family: 'Roboto', sans-serif;
            font-size: 1.8em; /* Subtitle size */
            font-weight: 700;
            color: #e0e0e0;
            margin: 0 0 10px 0;
        }

        /* Technology Description Styling */
        .tech-description {
            font-size: 1.3em; /* Normal text size */
            font-weight: 300;
            line-height: 1.5;
            color: #b0c4de;
            margin: 0;
        }

        /* Footer Bar */
        .footer-bar {
            width: 100%;
            height: 40px; /* Height of the footer bar */
            background-color: rgba(0, 0, 0, 0.2); /* Semi-transparent dark bar */
            position: absolute; /* Position relative to .slide */
            bottom: 0; /* Stick to the bottom of the slide */
            left: 0;
            display: flex;
            align-items: center;
            justify-content: flex-end; /* Push content to the right */
            padding-right: 40px; /* Padding for the right-aligned text */
            box-sizing: border-box;
            z-index: 10; /* Ensure it's on top */
        }

        /* Empty Footer Content (as per request) */
        .footer-bar .absolute {
            position: absolute; /* Position relative to .footer-bar */
            bottom: 8px; /* Equivalent to Tailwind's bottom-2 (approx 8px) */
            right: 16px; /* Equivalent to Tailwind's right-4 (approx 16px) */
            color: white;
            font-size: 0.875em; /* Equivalent to Tailwind's text-sm (approx 14px) */
        }
    </style>
</head>
<body>
    <div class="slide">
        <div class="content-area">
            <h1 class="slide-title">Technology Stack</h1>

            <div class="tech-stack-grid">
                <div class="tech-card">
                    <i class="fas fa-brain icon"></i>
                    <h2 class="tech-name">Language Model: Sentence Transformers</h2>
                    <p class="tech-description">`sentence-transformers/all-mpnet-base-v2` is chosen for its high accuracy and efficiency in generating robust sentence embeddings, crucial for semantic search.</p>
                </div>
                <div class="tech-card">
                    <i class="fas fa-database icon"></i>
                    <h2 class="tech-name">Vector Database: Pinecone</h2>
                    <p class="tech-description">Pinecone is selected for its exceptional scalability, speed, and ease of integration with our chosen cloud provider. Its proven performance in handling large-scale vector search makes it ideal.</p>
                </div>
                <div class="tech-card">
                    <i class="fas fa-cloud icon"></i>
                    <h2 class="tech-name">Cloud Provider: AWS</h2>
                    <p class="tech-description">Leveraging Amazon Web Services (AWS) for its robust infrastructure, comprehensive suite of services, and proven reliability, providing a scalable and secure foundation.</p>
                </div>
                <div class="tech-card">
                    <i class="fas fa-server icon"></i>
                    <h2 class="tech-name">Compute: AWS Lambda</h2>
                    <p class="tech-description">Utilizing AWS Lambda serverless functions for cost-effectiveness, automatic scaling, and efficient execution of embedding generation and API logic.</p>
                </div>
                <div class="tech-card">
                    <i class="fas fa-hdd icon"></i>
                    <h2 class="tech-name">Storage: AWS S3</h2>
                    <p class="tech-description">Amazon S3 provides highly durable, scalable, and secure object storage for all contract documents, ensuring data integrity and accessibility.</p>
                </div>
                <div class="tech-card">
                    <i class="fas fa-globe icon"></i>
                    <h2 class="tech-name">API Gateway: AWS API Gateway</h2>
                    <p class="tech-description">AWS API Gateway offers a secure, scalable, and fully managed service to expose the search functionality via a robust API endpoint.</p>
                </div>
            </div>
        </div>

        <div class="footer-bar">
            <div class="absolute bottom-2 right-4 text-white text-sm"></div>
        </div>
    </div>
</body>
</html>
"""
}

example_5 = \
{
"type" : "overflow",
"html" : \
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Return on Investment (ROI) - Intelligent Contract Document Search System</title>
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        /* General Body Styles */
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh; /* Ensure it takes full viewport height for centering */
            background-color: #f0f0f0; /* Light background for the page itself */
            font-family: 'Lato', sans-serif; /* Primary font */
            color: #ffffff; /* Default text color for the slide */
            overflow: hidden; /* Prevent scrollbars if slide is larger than viewport */
        }

        /* Slide Container - Defines 720p resolution */
        .slide {
            width: 1280px; /* 720p width */
            height: 720px; /* 720p height */
            background: linear-gradient(135deg, #1a2a3a 0%, #0f1a25 100%); /* Dark blue/grey gradient */
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); /* Subtle shadow for depth */
            display: flex;
            flex-direction: column;
            padding: 60px 80px; /* Internal padding for content */
            box-sizing: border-box; /* Include padding in width/height */
            position: relative; /* Crucial for absolute positioning of logo and footer */
            overflow: hidden; /* Ensure nothing spills out */
        }

        /* Main Content Area */
        .content-area {
            flex-grow: 1; /* Allows content to take available space */
            display: flex;
            flex-direction: column; /* Stack title and grid vertically */
            justify-content: flex-start; /* Align content to the top */
            align-items: flex-start; /* Align text to the left */
            text-align: left;
            padding-bottom: 0; /* No presenter info, so no need for bottom padding here */
            z-index: 1; /* Below logo */
        }

        /* Slide Title Styling (for all slides after title slide) */
        .slide-title {
            font-family: 'Roboto', sans-serif;
            font-size: 2.3em; /* Specified size */
            font-weight: 700;
            color: #e0e0e0;
            margin: 0 0 40px 0; /* Space below title */
            width: 100%; /* Ensure it takes full width */
        }

        /* ROI Content Grid Layout */
        .roi-content-grid {
            display: grid;
            grid-template-columns: 1fr 1.2fr; /* Left column for text, right for graph */
            gap: 60px; /* Gap between columns */
            width: 100%; /* Take full width of content area */
            flex-grow: 1; /* Allow grid to take remaining space */
            align-items: center; /* Vertically center content in grid cells */
        }

        /* Section Styling within the grid */
        .roi-section {
            background-color: rgba(255, 255, 255, 0.05); /* Slightly lighter background for sections */
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            height: 100%; /* Ensure sections fill their grid cell height */
            justify-content: center; /* Vertically center content within the section */
        }

        /* Section Heading Styling */
        .section-heading {
            font-family: 'Roboto', sans-serif;
            font-size: 1.8em; /* Subtitle size */
            font-weight: 700;
            color: #e0e0e0;
            margin: 0 0 20px 0;
            display: flex;
            align-items: center;
        }

        /* Icon Styling for Headings */
        .section-heading .icon {
            font-size: 1.5em; /* Larger icon for headings */
            margin-right: 15px;
            color: #66b3ff; /* Bright blue for icons */
        }

        /* List Styling for Quantified Benefits */
        .benefits-list {
            list-style: none;
            padding: 0;
            margin: 0;
            width: 100%;
        }

        .benefits-list li {
            font-size: 1.3em; /* Normal text size for short sentences */
            font-weight: 300;
            line-height: 1.5;
            color: #b0c4de;
            margin-bottom: 15px;
            display: flex;
            align-items: flex-start;
        }

        .benefits-list li:last-child {
            margin-bottom: 0;
        }

        /* Icon Styling for List Items */
        .benefits-list .list-icon {
            font-size: 1.3em;
            margin-right: 12px;
            color: #4CAF50; /* Green for checkmarks */
            flex-shrink: 0; /* Prevent icon from shrinking */
            padding-top: 2px; /* Align icon with text baseline */
        }

        /* ROI Calculation Details */
        .calculation-details p {
            font-size: 1.3em; /* Normal text size */
            font-weight: 300;
            line-height: 1.6;
            color: #b0c4de;
            margin: 0 0 10px 0;
        }

        .calculation-details .formula {
            font-family: 'Roboto Mono', monospace; /* Monospace for code/formula */
            background-color: rgba(0, 0, 0, 0.2);
            padding: 10px 15px;
            border-radius: 5px;
            margin: 20px 0;
            display: inline-block; /* To make padding/background apply correctly */
            font-size: 1.1em; /* Slightly smaller for formula */
            color: #e0e0e0;
        }

        .calculation-details .highlight {
            font-weight: 700;
            color: #66b3ff; /* Highlight color for numbers */
        }

        /* Graph Container */
        .graph-container {
            background-color: rgba(255, 255, 255, 0.05);
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%; /* Fill grid cell height */
        }

        /* SVG Styling */
        .roi-graph {
            width: 100%;
            height: 100%;
            max-width: 600px; /* Max width for the graph itself */
            max-height: 400px; /* Max height for the graph itself */
        }

        .roi-graph .axis-line {
            stroke: #b0c4de;
            stroke-width: 2;
        }

        .roi-graph .cost-line {
            stroke: #FF6347; /* Tomato red for cost */
            stroke-width: 4;
            fill: none;
        }

        .roi-graph .benefits-line {
            stroke: #4CAF50; /* Green for benefits */
            stroke-width: 4;
            fill: none;
        }

        .roi-graph .grid-line {
            stroke: rgba(255, 255, 255, 0.1);
            stroke-width: 1;
            stroke-dasharray: 5,5;
        }

        .roi-graph .label {
            font-family: 'Lato', sans-serif;
            font-size: 16px;
            fill: #b0c4de;
        }

        .roi-graph .breakeven-point {
            fill: #66b3ff;
            font-size: 18px;
            font-weight: 700;
        }

        /* Footer Bar */
        .footer-bar {
            width: 100%;
            height: 40px; /* Height of the footer bar */
            background-color: rgba(0, 0, 0, 0.2); /* Semi-transparent dark bar */
            position: absolute; /* Position relative to .slide */
            bottom: 0; /* Stick to the bottom of the slide */
            left: 0;
            display: flex;
            align-items: center;
            justify-content: flex-end; /* Push content to the right */
            padding-right: 40px; /* Padding for the right-aligned text */
            box-sizing: border-box;
            z-index: 10; /* Ensure it's on top */
        }

        /* Empty Footer Content (as per request) */
        .footer-bar .absolute {
            position: absolute; /* Position relative to .footer-bar */
            bottom: 8px; /* Equivalent to Tailwind's bottom-2 (approx 8px) */
            right: 16px; /* Equivalent to Tailwind's right-4 (approx 16px) */
            color: white;
            font-size: 0.875em; /* Equivalent to Tailwind's text-sm (approx 14px) */
        }
    </style>
</head>
<body>
    <div class="slide">
        <div class="content-area">
            <h1 class="slide-title">Return on Investment (ROI)</h1>

            <div class="roi-content-grid">
                <div class="roi-section">
                    <h2 class="section-heading"><i class="fas fa-chart-line icon"></i> Quantified Benefits</h2>
                    <ul class="benefits-list">
                        <li><i class="fas fa-dollar-sign list-icon"></i> Estimated <span class="highlight">$50,000</span> annual savings in legal review time.</li>
                        <li><i class="fas fa-shield-alt list-icon"></i> Potential <span class="highlight">$25,000</span> reduction in risk exposure due to improved compliance.</li>
                        <li><i class="fas fa-rocket list-icon"></i> Increased productivity leading to an estimated <span class="highlight">$30,000</span> in additional revenue.</li>
                    </ul>

                    <h2 class="section-heading" style="margin-top: 40px;"><i class="fas fa-calculator icon"></i> ROI Calculation</h2>
                    <div class="calculation-details">
                        <p>Total Estimated Benefits: <span class="highlight">$105,000</span> per year</p>
                        <p>Total Estimated Cost: <span class="highlight">[From previous slide]</span></p>
                        <p class="formula">ROI = (Total Benefits - Total Cost) / Total Cost</p>
                        <p>Estimated ROI of <span class="highlight">[Calculated ROI]%</span> within <span class="highlight">[Number]</span> years.</p>
                    </div>
                </div>

                <div class="graph-container">
                    <svg class="roi-graph" viewBox="0 0 600 400">
                        <!-- Background Grid Lines -->
                        <line class="grid-line" x1="50" y1="350" x2="550" y2="350" />
                        <line class="grid-line" x1="50" y1="250" x2="550" y2="250" />
                        <line class="grid-line" x1="50" y1="150" x2="550" y2="150" />
                        <line class="grid-line" x1="50" y1="50" x2="550" y2="50" />

                        <line class="grid-line" x1="150" y1="50" x2="150" y2="350" />
                        <line class="grid-line" x1="250" y1="50" x2="250" y2="350" />
                        <line class="grid-line" x1="350" y1="50" x2="350" y2="350" />
                        <line class="grid-line" x1="450" y1="50" x2="450" y2="350" />

                        <!-- Axes -->
                        <line class="axis-line" x1="50" y1="50" x2="50" y2="350" />
                        <line class="axis-line" x1="50" y1="350" x2="550" y2="350" />

                        <!-- Axis Labels -->
                        <text class="label" x="25" y="200" transform="rotate(-90 25 200)" text-anchor="middle">Cost/Benefit ($)</text>
                        <text class="label" x="300" y="380" text-anchor="middle">Time (Years)</text>

                        <!-- Y-axis ticks and labels (example values) -->
                        <text class="label" x="40" y="355" text-anchor="end">0</text>
                        <text class="label" x="40" y="255" text-anchor="end">50K</text>
                        <text class="label" x="40" y="155" text-anchor="end">100K</text>
                        <text class="label" x="40" y="55" text-anchor="end">150K</text>

                        <!-- X-axis ticks and labels (example years) -->
                        <text class="label" x="50" y="365" text-anchor="middle">0</text>
                        <text class="label" x="150" y="365" text-anchor="middle">1</text>
                        <text class="label" x="250" y="365" text-anchor="middle">2</text>
                        <text class="label" x="350" y="365" text-anchor="middle">3</text>
                        <text class="label" x="450" y="365" text-anchor="middle">4</text>
                        <text class="label" x="550" y="365" text-anchor="middle">5</text>

                        <!-- Cost Line (starts high, might flatten or slightly increase) -->
                        <!-- Example: Initial cost 100K, then slight maintenance -->
                        <polyline class="cost-line" points="50,150 150,140 250,135 350,130 450,125 550,120" />

                        <!-- Benefits Line (starts at 0, increases over time) -->
                        <!-- Example: Benefits start slow, then accelerate -->
                        <polyline class="benefits-line" points="50,350 150,280 250,200 350,100 450,70 550,50" />

                        <!-- Breakeven Point (intersection of lines) -->
                        <!-- Approximate intersection at (2.5 years, 130K) based on example points -->
                        <circle cx="290" cy="132" r="8" fill="#66b3ff" />
                        <text class="breakeven-point" x="300" y="120" text-anchor="start">Breakeven (~2.5 Yrs)</text>
                    </svg>
                </div>
            </div>
        </div>

        <div class="footer-bar">
            <div class="absolute bottom-2 right-4 text-white text-sm"></div>
        </div>
    </div>
</body>
</html>
"""
}

example_6 = \
{
"type" : "overflow",
"html" : \
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Security & Compliance - Intelligent Contract Document Search System</title>
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        /* General Body Styles */
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh; /* Ensure it takes full viewport height for centering */
            background-color: #f0f0f0; /* Light background for the page itself */
            font-family: 'Lato', sans-serif; /* Primary font */
            color: #ffffff; /* Default text color for the slide */
            overflow: hidden; /* Prevent scrollbars if slide is larger than viewport */
        }

        /* Slide Container - Defines 720p resolution */
        .slide {
            width: 1280px; /* 720p width */
            height: 720px; /* 720p height */
            background: linear-gradient(135deg, #1a2a3a 0%, #0f1a25 100%); /* Dark blue/grey gradient */
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); /* Subtle shadow for depth */
            display: flex;
            flex-direction: column;
            padding: 60px 80px; /* Internal padding for content */
            box-sizing: border-box; /* Include padding in width/height */
            position: relative; /* Crucial for absolute positioning of logo and footer */
            overflow: hidden; /* Ensure nothing spills out */
        }

        /* Main Content Area */
        .content-area {
            flex-grow: 1; /* Allows content to take available space */
            display: flex;
            flex-direction: column; /* Stack title and grid vertically */
            justify-content: flex-start; /* Align content to the top */
            align-items: flex-start; /* Align text to the left */
            text-align: left;
            padding-bottom: 0; /* No presenter info, so no need for bottom padding here */
            z-index: 1; /* Below logo */
        }

        /* Slide Title Styling (for all slides after title slide) */
        .slide-title {
            font-family: 'Roboto', sans-serif;
            font-size: 2.3em; /* Specified size */
            font-weight: 700;
            color: #e0e0e0;
            margin: 0 0 40px 0; /* Space below title */
            width: 100%; /* Ensure it takes full width */
        }

        /* Executive Summary Grid Layout (repurposed for general two-column layout) */
        .executive-summary-grid { /* This class name is from the agenda slide, but its styles are general enough */
            display: grid;
            grid-template-columns: auto auto; /* Two equal columns */
            grid-template-rows: auto auto; /* Rows adjust to content */
            gap: 40px 60px; /* Vertical and horizontal gap */
            width: 100%; /* Take full width of content area */
            flex-grow: 1; /* Allow grid to take remaining space */
        }

        /* Section Styling within the grid (repurposed for security/compliance sections) */
        .problem-section, /* These class names are from the agenda slide, but their styles are general enough */
        .solution-section,
        .benefits-section,
        .call-to-action-section,
        .security-section, /* New class for security measures */
        .compliance-section { /* New class for compliance */
            background-color: rgba(255, 255, 255, 0.05); /* Slightly lighter background for sections */
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            display: flex;
            flex-direction: column;
            align-items: flex-start;
        }

        /* Section Heading Styling */
        .section-heading {
            font-family: 'Roboto', sans-serif;
            font-size: 1.8em; /* Subtitle size */
            font-weight: 700;
            color: #e0e0e0;
            margin: 0 0 15px 0;
            display: flex;
            align-items: center;
        }

        /* Icon Styling for Headings */
        .section-heading .icon {
            font-size: 1.5em; /* Larger icon for headings */
            margin-right: 15px;
            color: #66b3ff; /* Bright blue for icons */
        }

        /* Normal Text Styling for Problem, Solution, Call to Action (repurposed for general text) */
        .section-text {
            font-size: 1.3em; /* Normal text size for short sentences */
            font-weight: 300;
            line-height: 1.5;
            color: #b0c4de;
            margin: 0;
        }

        /* Benefits List Styling (repurposed for general feature lists) */
        .benefits-list,
        .feature-list { /* New class for general feature lists */
            list-style: none;
            padding: 0;
            margin: 0;
            width: 100%;
        }

        .benefits-list li,
        .feature-list li { /* Apply to both existing and new list items */
            font-size: 1.3em; /* Adjusted to 1.3em for better readability as per instructions */
            font-weight: 400;
            color: #b0c4de;
            margin-bottom: 15px; /* Increased margin for better spacing */
            display: flex;
            align-items: flex-start;
            line-height: 1.4;
        }

        .benefits-list li:last-child,
        .feature-list li:last-child {
            margin-bottom: 0;
        }

        /* Icon Styling for List Items */
        .benefits-list .list-icon,
        .feature-list .list-icon { /* Apply to both existing and new list icons */
            font-size: 1.2em; /* Slightly larger for visibility */
            margin-right: 12px; /* Adjusted margin */
            color: #4CAF50; /* Green for checkmarks/success */
            flex-shrink: 0; /* Prevent icon from shrinking */
            padding-top: 2px; /* Align icon with text baseline */
        }

        /* Specific styling for the note section */
        .note-section {
            width: 100%;
            margin-top: 40px; /* Space above the note */
            padding: 20px 30px;
            background-color: rgba(255, 255, 255, 0.08); /* Slightly darker background for emphasis */
            border-left: 5px solid #66b3ff; /* Blue border for accent */
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            display: flex;
            align-items: center;
        }

        .note-text {
            font-size: 1.2em; /* Slightly larger for the note */
            font-weight: 400;
            color: #e0e0e0;
            margin: 0;
            line-height: 1.5;
        }

        .note-icon {
            font-size: 1.5em;
            color: #66b3ff; /* Blue for info icon */
            margin-right: 20px;
            flex-shrink: 0;
        }

        /* Footer Bar */
        .footer-bar {
            width: 100%;
            height: 40px; /* Height of the footer bar */
            background-color: rgba(0, 0, 0, 0.2); /* Semi-transparent dark bar */
            position: absolute; /* Position relative to .slide */
            bottom: 0; /* Stick to the bottom of the slide */
            left: 0;
            display: flex;
            align-items: center;
            justify-content: flex-end; /* Push content to the right */
            padding-right: 40px; /* Padding for the right-aligned text */
            box-sizing: border-box;
            z-index: 10; /* Ensure it's on top */
        }

        /* Empty Footer Content (as per request) */
        .footer-bar .absolute {
            position: absolute; /* Position relative to .footer-bar */
            bottom: 8px; /* Equivalent to Tailwind's bottom-2 (approx 8px) */
            right: 16px; /* Equivalent to Tailwind's right-4 (approx 16px) */
            color: white;
            font-size: 0.875em; /* Equivalent to Tailwind's text-sm (approx 14px) */
        }
    </style>
</head>
<body>
    <div class="slide">
        <div class="content-area">
            <h1 class="slide-title">Security & Compliance</h1>

            <div class="executive-summary-grid"> <!-- Reusing grid layout for two columns -->
                <div class="security-section">
                    <h2 class="section-heading"><i class="fas fa-shield-alt icon"></i> Security Measures</h2>
                    <ul class="feature-list">
                        <li><i class="fas fa-lock feature-list-icon" style="color: #FFD700;"></i> Data encryption at rest and in transit to protect sensitive contract information.</li>
                        <li><i class="fas fa-user-shield feature-list-icon" style="color: #FFD700;"></i> Role-based access control to restrict access to authorized personnel only.</li>
                        <li><i class="fas fa-clipboard-check feature-list-icon" style="color: #FFD700;"></i> Regular security audits and vulnerability assessments to identify and address potential threats.</li>
                        <li><i class="fas fa-network-wired feature-list-icon" style="color: #FFD700;"></i> Integration with existing security infrastructure for seamless authentication and authorization.</li>
                    </ul>
                </div>
                <div class="compliance-section">
                    <h2 class="section-heading"><i class="fas fa-gavel icon"></i> Compliance</h2>
                    <ul class="feature-list">
                        <li><i class="fas fa-balance-scale feature-list-icon" style="color: #FFD700;"></i> Compliance with relevant data privacy regulations, such as GDPR and CCPA.</li>
                        <li><i class="fas fa-file-contract feature-list-icon" style="color: #FFD700;"></i> Implementation of data retention policies to ensure compliance with legal requirements.</li>
                        <li><i class="fas fa-award feature-list-icon" style="color: #FFD700;"></i> Adherence to industry best practices for data security and privacy.</li>
                    </ul>
                </div>
            </div>

            <div class="note-section">
                <i class="fas fa-info-circle note-icon"></i>
                <p class="note-text">Security and compliance are paramount. We will work closely with your security team to ensure the system meets your specific requirements.</p>
            </div>
        </div>

        <div class="footer-bar">
            <div class="absolute bottom-2 right-4 text-white text-sm"></div>
        </div>
    </div>
</body>
</html>
"""
}

example_7 = \
{
"type" : "overflow",
"html" : \
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Conclusion - Intelligent Contract Document Search System</title>
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        /* General Body Styles */
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh; /* Ensure it takes full viewport height for centering */
            background-color: #f0f0f0; /* Light background for the page itself */
            font-family: 'Lato', sans-serif; /* Primary font */
            color: #ffffff; /* Default text color for the slide */
            overflow: hidden; /* Prevent scrollbars if slide is larger than viewport */
        }

        /* Slide Container - Defines 720p resolution */
        .slide {
            width: 1280px; /* 720p width */
            height: 720px; /* 720p height */
            background: linear-gradient(135deg, #1a2a3a 0%, #0f1a25 100%); /* Dark blue/grey gradient */
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); /* Subtle shadow for depth */
            display: flex;
            flex-direction: column;
            padding: 60px 80px; /* Internal padding for content */
            box-sizing: border-box; /* Include padding in width/height */
            position: relative; /* Crucial for absolute positioning of logo and footer */
            overflow: hidden; /* Ensure nothing spills out */
        }

        /* Main Content Area */
        .content-area {
            flex-grow: 1; /* Allows content to take available space */
            display: flex;
            flex-direction: column; /* Stack title and content vertically */
            justify-content: flex-start; /* Align content to the top */
            align-items: flex-start; /* Align text to the left */
            text-align: left;
            z-index: 1; /* Below logo */
        }

        /* Slide Title Styling (for all slides after title slide) */
        .slide-title {
            font-family: 'Roboto', sans-serif;
            font-size: 2.3em; /* Specified size */
            font-weight: 700;
            color: #e0e0e0;
            margin: 0 0 40px 0; /* Space below title */
            width: 100%; /* Ensure it takes full width */
        }

        /* Conclusion Content Container */
        .conclusion-container {
            display: flex;
            flex-direction: column;
            gap: 30px; /* Space between sections */
            width: 100%;
            max-width: 900px; /* Limit width for readability */
            margin: auto; /* Center the container horizontally */
            align-items: center; /* Center content within the container */
            text-align: center; /* Center text within the container */
        }

        /* Section Styling within the conclusion */
        .conclusion-section {
            background-color: rgba(255, 255, 255, 0.05); /* Slightly lighter background for sections */
            padding: 35px 45px; /* More padding for a substantial feel */
            border-radius: 12px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.25);
            width: 100%; /* Take full width of its parent (conclusion-container) */
            box-sizing: border-box;
        }

        /* Section Heading Styling */
        .section-heading {
            font-family: 'Roboto', sans-serif;
            font-size: 1.8em; /* Subtitle size */
            font-weight: 700;
            color: #e0e0e0;
            margin: 0 0 20px 0;
            display: flex;
            align-items: center;
            justify-content: center; /* Center heading with icon */
        }

        /* Icon Styling for Headings */
        .section-heading .icon {
            font-size: 1.6em; /* Larger icon for headings */
            margin-right: 15px;
            color: #66b3ff; /* Bright blue for icons */
        }

        /* Normal Text Styling for Conclusion */
        .section-text {
            font-size: 1.3em; /* Normal text size for short sentences */
            font-weight: 300;
            line-height: 1.6;
            color: #b0c4de;
            margin: 0;
        }

        /* Specific styling for Call to Action */
        .call-to-action-section {
            background: linear-gradient(45deg, #007bff, #0056b3); /* Stronger gradient for CTA */
            border: 2px solid #0056b3;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
            transform: translateY(0); /* Initial state for potential animation */
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        }

        .call-to-action-section:hover {
            transform: translateY(-5px); /* Slight lift on hover */
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.5);
        }

        .call-to-action-section .section-heading .icon {
            color: #ffffff; /* White icon for CTA */
        }

        .call-to-action-section .section-text {
            color: #e0e0e0; /* Lighter text for CTA */
            font-weight: 400;
        }

        /* Footer Bar */
        .footer-bar {
            width: 100%;
            height: 40px; /* Height of the footer bar */
            background-color: rgba(0, 0, 0, 0.2); /* Semi-transparent dark bar */
            position: absolute; /* Position relative to .slide */
            bottom: 0; /* Stick to the bottom of the slide */
            left: 0;
            display: flex;
            align-items: center;
            justify-content: flex-end; /* Push content to the right */
            padding-right: 40px; /* Padding for the right-aligned text */
            box-sizing: border-box;
            z-index: 10; /* Ensure it's on top */
        }

        /* Empty Footer Content (as per request) */
        .footer-bar .absolute {
            position: absolute; /* Position relative to .footer-bar */
            bottom: 8px; /* Equivalent to Tailwind's bottom-2 (approx 8px) */
            right: 16px; /* Equivalent to Tailwind's right-4 (approx 16px) */
            color: white;
            font-size: 0.875em; /* Equivalent to Tailwind's text-sm (approx 14px) */
        }
    </style>
</head>
<body>
    <div class="slide">
        <div class="content-area">
            <h1 class="slide-title">Conclusion</h1>

            <div class="conclusion-container">
                <div class="conclusion-section">
                    <h2 class="section-heading"><i class="fas fa-chart-line icon"></i> Transformative Impact</h2>
                    <p class="section-text">This AI-powered semantic search system will transform contract document management, leading to significantly improved accuracy, faster retrieval times, enhanced compliance, increased productivity, and better decision-making.</p>
                </div>

                <div class="conclusion-section">
                    <h2 class="section-heading"><i class="fas fa-dollar-sign icon"></i> Unlocking Value</h2>
                    <p class="section-text">By leveraging cutting-edge AI technologies and cloud services, this solution will deliver significant cost savings, reduce risk, and empower your employees to work more efficiently.</p>
                </div>

                <div class="conclusion-section call-to-action-section">
                    <h2 class="section-heading"><i class="fas fa-handshake icon"></i> Next Steps</h2>
                    <p class="section-text">We are confident that this solution will deliver significant value to the company. We recommend moving forward with the implementation of this project to unlock the full potential of your contract data.</p>
                </div>
            </div>
        </div>

        <div class="footer-bar">
            <div class="absolute bottom-2 right-4 text-white text-sm"></div>
        </div>
    </div>
</body>
</html>
"""
}

example_8 = \
{
"type" : "overflow",
"html" : \
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Intelligent Contract Document Retrieval System - The Problem: Quantifiable Impact</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        /* Global styles for the page background */
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: #0a0a1a; /* A very dark blue/charcoal for the overall page */
            font-family: 'Inter', sans-serif;
            color: #ffffff;
        }

        /* Slide Container - Defines the 720p slide dimensions and base style */
        .slide-container {
            width: 1280px; /* 720p width */
            height: 720px; /* 720p height */
            background: linear-gradient(135deg, #1a2a6c, #0f1a3d); /* Deep blue to dark charcoal gradient */
            color: #ffffff;
            display: flex;
            flex-direction: column;
            justify-content: space-between; /* Pushes content to top/middle and footer to bottom */
            align-items: center;
            padding: 60px 80px; /* Internal padding for content */
            box-sizing: border-box; /* Include padding in width/height */
            position: relative; /* For absolute positioning of footer */
            overflow: hidden; /* Ensures nothing spills out */
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5); /* Subtle shadow for depth */
            border-radius: 8px; /* Slightly rounded corners for a modern look */
        }

        /* Main Content Area - Wraps all slide content except footer */
        .main-slide-content {
            flex-grow: 1; /* Allows this area to take up available space */
            display: flex;
            flex-direction: column;
            width: 100%; /* Ensure it spans the width */
            justify-content: flex-start; /* Start content from the top */
            align-items: flex-start; /* Align items to the left by default */
        }

        /* Header Area for Slide Title */
        .header-area {
            width: 100%; /* Takes full width */
            text-align: left; /* Aligns text within its own box */
            margin-bottom: 30px; /* Space below title */
        }

        /* Slide Title Style */
        .slide-title {
            font-size: 2.3em; /* As requested */
            font-weight: 700;
            color: #ffffff;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
            margin: 0; /* Reset default margins */
        }

        /* Headline Section Style */
        .headline-section {
            width: 100%;
            text-align: center;
            margin-bottom: 40px; /* Space below headline */
        }

        /* Main Headline Style */
        .main-headline {
            font-size: 1.8em; /* Increased as it's a short sentence/headline */
            font-weight: 700;
            color: #87CEEB; /* A lighter blue for emphasis */
            line-height: 1.3;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
            margin: 0; /* Reset default margins */
        }

        /* Chart Section */
        .chart-section {
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            width: 100%;
            padding-top: 20px;
        }

        /* SVG Chart Container */
        .chart-container {
            width: 90%;
            max-width: 900px;
            height: 350px;
            background-color: rgba(255, 255, 255, 0.08);
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
            margin-bottom: 30px;
            position: relative; /* For absolute positioning of text */
        }

        .chart-container svg {
            width: 100%;
            height: 100%;
            overflow: visible; /* Allow text labels to extend */
        }

        /* SVG Bar Styles */
        .bar {
            fill: #ADD8E6; /* Light blue for bars */
            transition: fill 0.3s ease;
        }
        .bar.current {
            fill: #FF6347; /* Tomato red for current inefficiency */
        }
        .bar.projected {
            fill: #3CB371; /* Medium sea green for projected efficiency */
        }

        /* SVG Text Styles */
        .chart-label {
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            fill: #ffffff;
            opacity: 0.8;
        }
        .chart-value {
            font-family: 'Inter', sans-serif;
            font-size: 16px;
            font-weight: 700;
            fill: #ffffff;
        }
        .axis-label {
            font-family: 'Inter', sans-serif;
            font-size: 16px;
            font-weight: 700;
            fill: #ffffff;
        }

        /* Info Box for Cost */
        .info-box {
            background-color: rgba(255, 255, 255, 0.1);
            border-left: 5px solid #87CEEB;
            padding: 20px 30px;
            border-radius: 8px;
            width: 80%;
            max-width: 700px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
            margin-top: 20px;
        }

        .info-box p {
            font-size: 1.3em; /* Normal text size for this slide */
            line-height: 1.5;
            margin: 0;
            color: #ffffff;
        }

        .info-box strong {
            color: #87CEEB;
        }

        /* Footer Bar - As specified in the request */
        .footer-bar {
            width: 100%;
            height: 40px; /* A bit taller for better visual presence */
            background-color: rgba(0, 0, 0, 0.2); /* Semi-transparent dark background */
            position: absolute; /* Positioned relative to .slide-container */
            bottom: 0;
            left: 0;
            display: flex; /* Use flexbox for internal alignment */
            align-items: center; /* Vertically center content */
            padding: 0 20px; /* Padding for content inside footer */
            box-sizing: border-box;
        }

        /* Footer Text - As specified in the request */
        .footer-bar div {
            position: absolute; /* Absolute position within the footer bar */
            bottom: 8px; /* Equivalent to bottom-2 (assuming 1 unit = 4px) */
            right: 16px; /* Equivalent to right-4 (assuming 1 unit = 4px) */
            color: rgba(255, 255, 255, 0.6); /* Slightly transparent white */
            font-size: 0.8em; /* Equivalent to text-sm */
        }
    </style>
</head>
<body>
    <div class="slide-container">
        <div class="main-slide-content">
            <div class="header-area">
                <h1 class="slide-title">The Problem: Quantifiable Impact</h1>
            </div>

            <div class="headline-section">
                <h2 class="main-headline">The Hidden Costs of Manual Contract Retrieval</h2>
            </div>

            <div class="chart-section">
                <div class="chart-container">
                    <svg viewBox="0 0 800 300" preserveAspectRatio="xMidYMid meet">
                        <!-- Y-axis (Time in minutes) -->
                        <line x1="100" y1="250" x2="100" y2="50" stroke="#ffffff" stroke-width="2" opacity="0.6"/>
                        <text x="70" y="150" class="axis-label" transform="rotate(-90 70 150)">Time per Search (Minutes)</text>
                        <text x="90" y="255" class="chart-label">0</text>
                        <text x="80" y="205" class="chart-label">10</text>
                        <text x="80" y="155" class="chart-label">20</text>
                        <text x="80" y="105" class="chart-label">30</text>

                        <!-- X-axis (Scenarios) -->
                        <line x1="100" y1="250" x2="700" y2="250" stroke="#ffffff" stroke-width="2" opacity="0.6"/>
                        <text x="400" y="280" class="axis-label" text-anchor="middle">Search Scenarios</text>

                        <!-- Bar 1: Current Search Time (30 minutes) -->
                        <rect class="bar current" x="200" y="50" width="100" height="200" rx="5" ry="5"/>
                        <text x="250" y="40" text-anchor="middle" class="chart-value">30 min</text>
                        <text x="250" y="265" text-anchor="middle" class="chart-label">Current</text>

                        <!-- Bar 2: Projected Search Time (3 minutes) -->
                        <rect class="bar projected" x="500" y="230" width="100" height="20" rx="5" ry="5"/>
                        <text x="550" y="220" text-anchor="middle" class="chart-value">3 min</text>
                        <text x="550" y="265" text-anchor="middle" class="chart-label">Projected</text>

                        <!-- Legend -->
                        <rect x="650" y="50" width="20" height="15" fill="#FF6347" rx="3" ry="3"/>
                        <text x="680" y="62" class="chart-label">Current Inefficiency</text>
                        <rect x="650" y="80" width="20" height="15" fill="#3CB371" rx="3" ry="3"/>
                        <text x="680" y="92" class="chart-label">Projected Efficiency</text>
                    </svg>
                </div>

                <div class="info-box">
                    <p>With an average of <strong>50 contract searches per week</strong>, the current inefficiency translates to approximately <strong>22.5 hours of lost productivity weekly</strong>, costing the company an estimated <strong>$58,500 annually</strong> in employee time.</p>
                </div>
            </div>
        </div>

        <div class="footer-bar">
            <div></div>
        </div>
    </div>
</body>
</html>
"""
}

example_9 = \
{
"type" : "overflow",
"html" : \
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Our Solution: AI-Powered Semantic Search</title>
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
            min-height: 100vh; /* Ensures the slide is vertically centered on the page */
            background-color: #f0f0f0; /* Light background for the area outside the slide */
            font-family: 'Roboto', sans-serif; /* Modern, clean sans-serif font */
            overflow: hidden; /* Prevents scrollbars if the slide perfectly fits the viewport */
        }

        /* Styles for the main slide container */
        .slide-container {
            width: 1280px; /* 720p resolution width */
            height: 720px; /* 720p resolution height */
            background: linear-gradient(135deg, #1a2a3a 0%, #0a1a2a 100%); /* Deep navy/charcoal gradient for a professional, high-tech feel */
            color: #e0e0e0; /* Light gray for general text, ensuring good contrast */
            display: flex;
            flex-direction: column;
            justify-content: space-between; /* Distributes content and pushes footer to bottom */
            padding: 60px; /* Generous padding around the content for a clean look */
            box-sizing: border-box; /* Includes padding in the width/height calculation */
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); /* Subtle shadow for depth and professionalism */
            border-radius: 8px; /* Slightly rounded corners for a modern touch */
        }

        /* Styles for the main content area */
        .slide-content {
            flex-grow: 1; /* Allows this section to take up available space */
            display: flex;
            flex-direction: column;
            justify-content: flex-start; /* Align content to the top */
            align-items: flex-start; /* Align content to the left */
            text-align: left; /* Default text alignment */
            width: 100%; /* Ensure it takes full width of padding area */
            padding-top: 0; /* Remove extra padding from title slide */
        }

        /* Styles for the main slide title */
        .slide-title {
            font-size: 2.3em; /* Specified title size */
            font-weight: 700; /* Bold for emphasis */
            color: #ffffff; /* Pure white for maximum impact */
            margin-bottom: 30px; /* Space below title */
            line-height: 1.2;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* Subtle text shadow for depth */
            align-self: flex-start; /* Ensure it aligns to the start (left) */
        }

        /* Styles for the introductory text section */
        .intro-text {
            margin-bottom: 40px;
            width: 100%;
        }

        .intro-text p {
            font-size: 1.3em; /* Subtitle size for key points */
            color: #e0e0e0;
            line-height: 1.6;
            margin-bottom: 15px;
            display: flex;
            align-items: flex-start;
            gap: 15px;
        }

        .intro-text p .icon {
            font-size: 1.2em;
            color: #007bff; /* Accent color for icons */
            flex-shrink: 0;
            padding-top: 2px;
        }

        /* Styles for the comparison container */
        .comparison-container {
            display: flex;
            justify-content: space-around;
            align-items: flex-start; /* Align items to the top */
            width: 100%;
            flex-grow: 1; /* Allow it to take up remaining space */
            gap: 40px; /* Space between the two search boxes */
        }

        /* Styles for individual search boxes */
        .search-box {
            background-color: rgba(255, 255, 255, 0.07); /* Slightly transparent background */
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
            flex: 1; /* Allow boxes to grow and shrink */
            min-width: 45%; /* Ensure they don't get too small */
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .search-box.keyword {
            border-left: 5px solid #dc3545; /* Red accent for keyword search (problematic) */
        }

        .search-box.semantic {
            border-left: 5px solid #28a745; /* Green accent for semantic search (solution) */
        }

        .search-box h3 {
            font-size: 1.8em; /* Prominent title for search type */
            font-weight: 700;
            color: #ffffff;
            margin-top: 0;
            margin-bottom: 25px;
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .search-box h3 .icon {
            font-size: 1.2em;
            color: #007bff; /* Accent color for icons */
        }

        .query-input {
            background-color: rgba(0, 0, 0, 0.3);
            color: #ffffff;
            padding: 15px 20px;
            border-radius: 5px;
            width: 90%;
            margin-bottom: 30px;
            font-size: 1.1em;
            border: 1px solid rgba(255, 255, 255, 0.2);
            text-align: left;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .query-input i {
            color: #b0c4de;
        }

        .results-list {
            list-style: none;
            padding: 0;
            width: 100%;
            text-align: left;
        }

        .results-list li {
            background-color: rgba(255, 255, 255, 0.03);
            padding: 12px 15px;
            margin-bottom: 10px;
            border-radius: 5px;
            font-size: 1.1em;
            display: flex;
            align-items: center;
            gap: 10px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }

        .results-list li.relevant {
            background-color: rgba(40, 167, 69, 0.2); /* Greenish tint for relevant */
            border-left: 4px solid #28a745;
        }

        .results-list li.irrelevant {
            background-color: rgba(220, 53, 69, 0.1); /* Reddish tint for irrelevant */
            border-left: 4px solid #dc3545;
        }

        .results-list li i {
            font-size: 0.9em;
            flex-shrink: 0;
        }

        .results-list li.relevant i {
            color: #28a745;
        }

        .results-list li.irrelevant i {
            color: #dc3545;
        }

        /* Styles for the empty footer bar */
        .footer-bar {
            width: 100%;
            margin-top: auto; /* Pushes the footer to the very bottom */
            position: relative;
            height: 20px; /* Defines the height of the footer area */
            border-top: 1px solid rgba(255, 255, 255, 0.1); /* A subtle separator line */
        }

        /* Styles for the absolute positioned empty div within the footer */
        .footer-bar .absolute {
            position: absolute;
            bottom: 8px; /* Positioned from the bottom of its relative parent */
            right: 16px; /* Positioned from the right of its relative parent */
            color: #a0a0a0; /* Matches other info text color */
            font-size: 0.9em; /* Slightly smaller font size */
        }
    </style>
</head>
<body>
    <div class="slide-container">
        <div class="slide-content">
            <h1 class="slide-title">Our Solution: AI-Powered Semantic Search</h1>

            <div class="intro-text">
                <p><i class="fas fa-lightbulb icon"></i> Semantic search understands the *meaning* and *intent* behind your queries, not just matching keywords.</p>
                <p><i class="fas fa-brain icon"></i> It leverages cutting-edge AI technologies, including Transformer models, to analyze the context and relationships within contract documents.</p>
                <p><i class="fas fa-search-plus icon"></i> This allows for more accurate and relevant search results, even when using synonyms, paraphrases, or complex legal terminology.</p>
            </div>

            <div class="comparison-container">
                <div class="search-box keyword">
                    <h3><i class="fas fa-keyboard icon"></i> Traditional Keyword Search</h3>
                    <div class="query-input">
                        <i class="fas fa-search"></i> Termination Clause
                    </div>
                    <ul class="results-list">
                        <li class="relevant"><i class="fas fa-check-circle"></i> Contract A: Termination Clause - Section 5.1</li>
                        <li class="relevant"><i class="fas fa-check-circle"></i> Contract B: Early Termination Policy</li>
                        <li class="irrelevant"><i class="fas fa-times-circle"></i> Contract C: Clause on Data Security</li>
                        <li class="irrelevant"><i class="fas fa-times-circle"></i> Contract D: Project Termination Report</li>
                    </ul>
                </div>

                <div class="search-box semantic">
                    <h3><i class="fas fa-magic icon"></i> AI-Powered Semantic Search</h3>
                    <div class="query-input">
                        <i class="fas fa-search"></i> Termination Clause
                    </div>
                    <ul class="results-list">
                        <li class="relevant"><i class="fas fa-check-circle"></i> Contract A: Termination Clause - Section 5.1</li>
                        <li class="relevant"><i class="fas fa-check-circle"></i> Contract B: Early Termination Policy</li>
                        <li class="relevant"><i class="fas fa-check-circle"></i> Contract E: Agreement Cancellation Terms</li>
                        <li class="relevant"><i class="fas fa-check-circle"></i> Contract F: End of Contract Procedures</li>
                    </ul>
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
}

example_10 = \
{
"type" : "overflow",
"html" : \
"""
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
            min-height: 100vh; /* Ensures the slide is vertically centered on the page */
            background-color: #f0f0f0; /* Light background for the area outside the slide */
            font-family: 'Roboto', sans-serif; /* Modern, clean sans-serif font */
            overflow: hidden; /* Prevents scrollbars if the slide perfectly fits the viewport */
        }

        /* Styles for the main slide container */
        .slide-container {
            width: 1280px; /* 720p resolution width */
            height: 720px; /* 720p resolution height */
            background: linear-gradient(135deg, #1a2a3a 0%, #0a1a2a 100%); /* Deep navy/charcoal gradient for a professional, high-tech feel */
            color: #e0e0e0; /* Light gray for general text, ensuring good contrast */
            display: flex;
            flex-direction: column;
            justify-content: space-between; /* Distributes content and pushes footer to bottom */
            padding: 60px; /* Generous padding around the content for a clean look */
            box-sizing: border-box; /* Includes padding in the width/height calculation */
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); /* Subtle shadow for depth and professionalism */
            border-radius: 8px; /* Slightly rounded corners for a modern touch */
        }

        /* Styles for the main content area */
        .slide-content {
            flex-grow: 1; /* Allows this section to take up available space */
            display: flex;
            flex-direction: column;
            justify-content: flex-start; /* Align content to the top */
            align-items: flex-start; /* Align content to the left */
            text-align: left; /* Default text alignment */
            width: 100%; /* Ensure it takes full width of padding area */
            padding-top: 0; /* Remove extra padding from title slide */
        }

        /* Styles for the main slide title (e.g., "Executive Summary") */
        .slide-title {
            font-size: 2.3em; /* Specified title size */
            font-weight: 700; /* Bold for emphasis */
            color: #ffffff; /* Pure white for maximum impact */
            margin-bottom: 40px; /* Space below title */
            line-height: 1.2;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* Subtle text shadow for depth */
            align-self: flex-start; /* Ensure it aligns to the start (left) */
        }

        /* Container for the summary sections using a grid layout */
        .summary-sections {
            display: grid;
            grid-template-columns: auto auto; /* Two equal columns as requested */
            grid-template-rows: auto auto auto; /* Three rows for problem/solution, benefits, call to action */
            gap: 40px; /* Space between grid items */
            width: 100%;
            flex-grow: 1; /* Allow it to take up available space */
        }

        /* Styles for individual content sections (Problem, Solution, Benefits, CTA) */
        .section {
            background-color: rgba(255, 255, 255, 0.05); /* Slightly transparent background for sections */
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            display: flex;
            flex-direction: column;
            justify-content: flex-start; /* Align content to top within section */
        }

        /* Styles for section headings (e.g., "The Problem") */
        .section h3 {
            font-size: 1.8em; /* Subtitle size for section headings */
            color: #ffffff;
            margin-top: 0;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
        }

        /* Styles for normal text within sections */
        .section p, .section ul {
            font-size: 1.3em; /* Normal text size for content */
            color: #e0e0e0;
            line-height: 1.5;
            margin-bottom: 0; /* Remove default margin for last paragraph */
        }

        /* Specific grid placement for Problem and Solution */
        .section.problem {
            grid-column: 1 / 2; /* First column */
            grid-row: 1 / 2; /* First row */
        }

        .section.solution {
            grid-column: 2 / 3; /* Second column */
            grid-row: 1 / 2; /* First row */
        }

        /* Specific grid placement for Key Benefits (spans both columns) */
        .section.benefits {
            grid-column: 1 / 3; /* Span both columns */
            grid-row: 2 / 3; /* Second row */
        }

        /* Styles for the benefits list */
        .section ul {
            list-style: none; /* Remove default bullet points */
            padding-left: 0;
            margin-top: 10px;
        }

        .section ul li {
            margin-bottom: 10px;
            display: flex;
            align-items: flex-start; /* Align icon and text at the top */
        }

        /* Specific grid placement for Call to Action (spans both columns) */
        .section.call-to-action {
            grid-column: 1 / 3; /* Span both columns */
            grid-row: 3 / 4; /* Third row */
            text-align: center; /* Center the call to action text */
            background: linear-gradient(90deg, #007bff, #0056b3); /* A more prominent background for CTA */
            color: #ffffff;
            padding: 30px;
            justify-content: center; /* Center content vertically within CTA section */
        }

        .call-to-action p {
            font-size: 1.4em; /* Slightly larger for CTA text */
            font-weight: 400;
        }

        /* Icon styling for section headings */
        .icon {
            margin-right: 15px; /* More space for icons in headings */
            font-size: 1.2em; /* Slightly larger than text for headings */
            color: #007bff; /* Accent color for icons */
        }

        /* Icon styling for list items */
        .icon-small {
            margin-right: 10px;
            font-size: 1em; /* Standard size for list item icons */
            color: #28a745; /* Green for checkmarks */
            flex-shrink: 0; /* Prevent icon from shrinking */
            padding-top: 2px; /* Align icon with text baseline */
        }

        /* Styles for the empty footer bar */
        .footer-bar {
            width: 100%;
            margin-top: auto; /* Pushes the footer to the very bottom */
            position: relative;
            height: 20px; /* Defines the height of the footer area */
            border-top: 1px solid rgba(255, 255, 255, 0.1); /* A subtle separator line */
        }

        /* Styles for the absolute positioned empty div within the footer */
        .footer-bar .absolute {
            position: absolute;
            bottom: 8px; /* Positioned from the bottom of its relative parent */
            right: 16px; /* Positioned from the right of its relative parent */
            color: #a0a0a0; /* Matches other info text color */
            font-size: 0.9em; /* Slightly smaller font size */
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
                    <p>Finding relevant contract documents is currently slow, inaccurate, and relies heavily on manual keyword searches, leading to missed information and potential risks.</p>
                </div>
                <div class="section solution">
                    <h3><i class="fas fa-lightbulb icon"></i> The Solution</h3>
                    <p>We propose an AI-powered semantic search system that understands the *meaning* of contracts and queries, delivering highly relevant results quickly.</p>
                </div>
                <div class="section benefits">
                    <h3><i class="fas fa-star icon"></i> Key Benefits</h3>
                    <ul>
                        <li><i class="fas fa-check-circle icon-small"></i> Up to 90% Improvement in Search Accuracy</li>
                        <li><i class="fas fa-check-circle icon-small"></i> Reduce Contract Retrieval Time by 75%</li>
                        <li><i class="fas fa-check-circle icon-small"></i> Minimize Risk of Non-Compliance and Missed Obligations</li>
                        <li><i class="fas fa-check-circle icon-small"></i> Empower Employees with Faster Access to Critical Information</li>
                    </ul>
                </div>
                <div class="section call-to-action">
                    <h3><i class="fas fa-rocket icon"></i> Call to Action</h3>
                    <p>This proposal outlines a plan to transform contract document management, leading to significant cost savings, improved decision-making, and a stronger competitive advantage.</p>
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
}

example_11 = \
{
"type" : "normal",
"html" : \
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Intelligent Contract Document Retrieval System - Executive Summary</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        /* Global styles for the page background */
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: #0a0a1a; /* A very dark blue/charcoal for the overall page */
            font-family: 'Inter', sans-serif;
            color: #ffffff;
        }

        /* Slide Container - Defines the 720p slide dimensions and base style */
        .slide-container {
            width: 1280px; /* 720p width */
            height: 720px; /* 720p height */
            background: linear-gradient(135deg, #1a2a6c, #0f1a3d); /* Deep blue to dark charcoal gradient */
            color: #ffffff;
            display: flex;
            flex-direction: column;
            justify-content: space-between; /* Pushes content to top/middle and footer to bottom */
            align-items: center;
            padding: 60px 80px; /* Internal padding for content */
            box-sizing: border-box; /* Include padding in width/height */
            position: relative; /* For absolute positioning of footer */
            overflow: hidden; /* Ensures nothing spills out */
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5); /* Subtle shadow for depth */
            border-radius: 8px; /* Slightly rounded corners for a modern look */
        }

        /* Main Content Area - Wraps all slide content except footer */
        .main-slide-content {
            flex-grow: 1; /* Allows this area to take up available space */
            display: flex;
            flex-direction: column;
            width: 100%; /* Ensure it spans the width */
            justify-content: flex-start; /* Start content from the top */
            align-items: flex-start; /* Align items to the left by default */
        }

        /* Header Area for Slide Title */
        .header-area {
            width: 100%; /* Takes full width */
            text-align: left; /* Aligns text within its own box */
            margin-bottom: 30px; /* Space below title */
        }

        /* Slide Title Style */
        .slide-title {
            font-size: 2.3em; /* As requested */
            font-weight: 700;
            color: #ffffff;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
            margin: 0; /* Reset default margins */
        }

        /* Headline Section Style */
        .headline-section {
            width: 100%;
            text-align: center;
            margin-bottom: 40px; /* Space below headline */
        }

        /* Main Headline Style */
        .main-headline {
            font-size: 1.8em; /* Increased as it's a short sentence/headline */
            font-weight: 700;
            color: #87CEEB; /* A lighter blue for emphasis */
            line-height: 1.3;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
            margin: 0; /* Reset default margins */
        }

        /* Content Grid for main points */
        .content-grid {
            display: grid;
            grid-template-columns: auto auto; /* As requested */
            grid-template-rows: auto auto; /* As requested */
            gap: 30px; /* Space between grid items */
            width: 100%;
            max-width: 1000px; /* Max width for the grid to look good */
            margin: 0 auto; /* Center the grid horizontally */
            flex-grow: 1; /* Allow grid to take up remaining vertical space */
            align-items: start; /* Align items to the start of their grid cells */
            justify-content: center; /* Center the grid itself if it doesn't fill max-width */
        }

        /* Style for each grid item */
        .grid-item {
            background-color: rgba(255, 255, 255, 0.08); /* Slightly transparent white */
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
            display: flex;
            flex-direction: column;
            align-items: flex-start; /* Align content within item to the left */
            text-align: left;
            height: 100%; /* Ensure items fill their grid cell height */
            box-sizing: border-box; /* Include padding in height */
        }

        /* Icon Style */
        .icon, .icon-group .icon {
            font-size: 2.5em;
            margin-bottom: 15px;
            color: #87CEEB; /* Light blue for icons */
            line-height: 1; /* Prevent extra space around icons */
        }

        /* Icon Group for multiple icons */
        .icon-group {
            display: flex;
            gap: 10px;
            margin-bottom: 15px;
        }

        /* Item Subtitle Style */
        .item-subtitle {
            font-size: 1.3em; /* As requested */
            font-weight: 700;
            margin-bottom: 10px;
            color: #ADD8E6; /* Slightly different blue for subtitles */
            margin-top: 0; /* Reset default margins */
        }

        /* Item Text Style */
        .item-text {
            font-size: 0.9em; /* As requested */
            line-height: 1.6;
            opacity: 0.9;
            margin: 0; /* Reset default margins */
        }

        /* Footer Bar - As specified in the request */
        .footer-bar {
            width: 100%;
            height: 40px; /* A bit taller for better visual presence */
            background-color: rgba(0, 0, 0, 0.2); /* Semi-transparent dark background */
            position: absolute; /* Positioned relative to .slide-container */
            bottom: 0;
            left: 0;
            display: flex; /* Use flexbox for internal alignment */
            align-items: center; /* Vertically center content */
            padding: 0 20px; /* Padding for content inside footer */
            box-sizing: border-box;
        }

        /* Footer Text - As specified in the request */
        .footer-bar div {
            position: absolute; /* Absolute position within the footer bar */
            bottom: 8px; /* Equivalent to bottom-2 (assuming 1 unit = 4px) */
            right: 16px; /* Equivalent to right-4 (assuming 1 unit = 4px) */
            color: rgba(255, 255, 255, 0.6); /* Slightly transparent white */
            font-size: 0.8em; /* Equivalent to text-sm */
        }
    </style>
</head>
<body>
    <div class="slide-container">
        <div class="main-slide-content">
            <div class="header-area">
                <h1 class="slide-title">Executive Summary</h1>
            </div>

            <div class="headline-section">
                <h2 class="main-headline">Streamlining Contract Management with AI-Powered Search</h2>
            </div>

            <div class="content-grid">
                <div class="grid-item problem-item">
                    <div class="icon" role="img" aria-label="Warning sign icon">&#x1F6A8;</div>
                    <h3 class="item-subtitle">Problem:</h3>
                    <p class="item-text">Current contract retrieval is slow, inefficient, and prone to human error, leading to missed deadlines and potential legal risks. Average search time is currently 30 minutes per contract.</p>
                </div>
                <div class="grid-item solution-item">
                    <div class="icon" role="img" aria-label="Robot icon">&#x1F916;</div>
                    <h3 class="item-subtitle">Solution:</h3>
                    <p class="item-text">An intelligent system leveraging LLMs and vector databases for semantic search, dramatically improving accuracy and speed.</p>
                </div>
                <div class="grid-item benefits-item">
                    <div class="icon" role="img" aria-label="Flexed biceps icon">&#x1F4AA;</div>
                    <h3 class="item-subtitle">Key Benefits:</h3>
                    <p class="item-text">Reduced search time (to 3 minutes on average), increased accuracy (80% improvement), enhanced efficiency (freeing up 10 hours of employee time per week), minimized legal risks.</p>
                </div>
                <div class="grid-item cost-timeline-item">
                    <div class="icon-group">
                        <span class="icon" role="img" aria-label="Money bag icon">&#x1F4B0;</span>
                        <span class="icon" role="img" aria-label="Stopwatch icon">&#x23F1;</span>
                    </div>
                    <h3 class="item-subtitle">Cost & Timeline:</h3>
                    <p class="item-text">Project cost and timeline details will be provided in subsequent slides.</p>
                </div>
            </div>
        </div>

        <div class="footer-bar">
            <div></div>
        </div>
    </div>
</body>
</html>
"""
}

example_12 = \
{
"type" : "normal",
"html" : \
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Problem: The Business Impact - Intelligent Contract Document Search System</title>
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
            min-height: 100vh; /* Ensures the slide is vertically centered on the page */
            background-color: #f0f0f0; /* Light background for the area outside the slide */
            font-family: 'Roboto', sans-serif; /* Modern, clean sans-serif font */
            overflow: hidden; /* Prevents scrollbars if the slide perfectly fits the viewport */
        }

        /* Styles for the main slide container */
        .slide-container {
            width: 1280px; /* 720p resolution width */
            height: 720px; /* 720p resolution height */
            background: linear-gradient(135deg, #1a2a3a 0%, #0a1a2a 100%); /* Deep navy/charcoal gradient for a professional, high-tech feel */
            color: #e0e0e0; /* Light gray for general text, ensuring good contrast */
            display: flex;
            flex-direction: column;
            justify-content: space-between; /* Distributes content and pushes footer to bottom */
            padding: 30px 40px; /* Reduced vertical padding from 40px to 30px to ensure content fits */
            box-sizing: border-box; /* Includes padding in the width/height calculation */
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); /* Subtle shadow for depth and professionalism */
            border-radius: 8px; /* Slightly rounded corners for a modern touch */
        }

        /* Styles for the main content area */
        .slide-content {
            flex-grow: 1; /* Allows this section to take up available space */
            display: flex;
            flex-direction: column;
            justify-content: flex-start; /* Align content to the top */
            align-items: flex-start; /* Align content to the left */
            text-align: left; /* Default text alignment */
            width: 100%; /* Ensure it takes full width of padding area */
            padding-top: 0; /* Remove extra padding from title slide */
        }

        /* Styles for the main slide title */
        .slide-title {
            font-size: 2.3em; /* As requested, prominent title size */
            font-weight: 700; /* Bold for emphasis */
            color: #ffffff; /* Pure white for maximum impact */
            margin-bottom: 20px; /* Reduced from 30px to create more vertical space */
            line-height: 1.2;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* Subtle text shadow for depth */
            align-self: flex-start; /* Ensure it aligns to the start (left) */
        }

        /* Styles for the problem points container */
        .problem-points {
            display: flex;
            flex-direction: column;
            gap: 15px; /* Reduced from 25px to create more vertical space between points */
            width: 90%; /* Adjust width to leave some margin */
            margin-left: 20px; /* Indent slightly */
        }

        /* Styles for individual problem points */
        .problem-point {
            display: flex;
            align-items: flex-start; /* Align icon and text at the top */
            font-size: 1.5em; /* Subtitle size for main points */
            color: #e0e0e0;
            line-height: 1.4;
        }

        .problem-point .icon {
            margin-right: 20px;
            font-size: 1.2em; /* Slightly smaller than text for visual balance */
            color: #ff6b6b; /* A warning/problem color (reddish) */
            flex-shrink: 0; /* Prevent icon from shrinking */
            padding-top: 5px; /* Adjust vertical alignment */
        }

        /* Styles for the strategic goals connection */
        .strategic-goals {
            margin-top: 30px; /* Reduced from 50px to create more vertical space */
            width: 90%;
            font-size: 1.3em; /* Normal text size, but slightly larger for emphasis */
            color: #b0c4de; /* A light blue-gray for a sophisticated accent */
            font-weight: 300;
            padding-left: 20px; /* Align with bullet points */
            border-left: 4px solid #007bff; /* Accent line */
            padding-left: 25px;
        }

        /* Styles for the empty footer bar */
        .footer-bar {
            width: 100%;
            margin-top: auto; /* Pushes the footer to the very bottom */
            position: relative;
            height: 20px; /* Defines the height of the footer area */
            border-top: 1px solid rgba(255, 255, 255, 0.1); /* A subtle separator line */
        }

        /* Styles for the absolute positioned empty div within the footer */
        .footer-bar .absolute {
            position: absolute;
            bottom: 8px; /* Positioned from the bottom of its relative parent */
            right: 16px; /* Positioned from the right of its relative parent */
            color: #a0a0a0; /* Matches other info text color */
            font-size: 0.9em; /* Slightly smaller font size */
        }
    </style>
</head>
<body>
    <div class="slide-container">
        <div class="slide-content">
            <h1 class="slide-title">The Problem: The Business Impact</h1>

            <div class="problem-points">
                <div class="problem-point">
                    <i class="fas fa-hourglass-half icon"></i>
                    <p>Estimated <strong>20 hours/week</strong> spent by legal and contract management teams searching for specific contract clauses.</p>
                </div>
                <div class="problem-point">
                    <i class="fas fa-gavel icon"></i>
                    <p>Potential <strong>15% reduction</strong> in legal review time by providing instant access to relevant contract information.</p>
                </div>
                <div class="problem-point">
                    <i class="fas fa-exclamation-triangle icon"></i>
                    <p>Risk of <strong>$5 million</strong> in potential penalties due to missed contract clauses or non-compliance.</p>
                </div>
                <div class="problem-point">
                    <i class="fas fa-handshake-slash icon"></i>
                    <p>Delayed deal closures due to slow contract retrieval and review processes.</p>
                </div>
            </div>

            <div class="strategic-goals">
                <p>This inefficiency directly impacts our ability to <strong>accelerate revenue growth</strong>, <strong>improve risk management</strong>, and <strong>ensure regulatory compliance</strong>.</p>
            </div>
        </div>

        <div class="footer-bar w-full mt-auto relative">
            <div class="absolute bottom-2 right-4 text-white text-sm"></div>
        </div>
    </div>
</body>
</html>
"""
}

samples = [
    example_1,
    example_2,
    example_3,
    example_4,
    example_5,
    example_6,
    example_7,
    example_8,
    example_9,
    example_10,
    example_11,
    example_12
]