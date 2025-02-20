import streamlit as st
import pandas as pd


st.set_page_config(page_title="My App", layout="wide")

# Custom CSS to increase the content width
st.markdown(
    """
     (<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">)
    <style>
        .main .block-container {
            max-width: 50%!important; /* Adjust width (default ~50%) */
            padding: 1rem;  /* Adjust padding */
        }

    </style>
    """,
    unsafe_allow_html=True
)

# Inject Custom CSS
st.markdown(
    """
    <style>
        /* Set background color to white */
        .stApp {
            background-color: white !important;
        }
        
        /* Ensure text is black */
        .stMarkdown, .css-1d391kg {
            color: black !important;
        }
        
        /* Adjust containers to remove any shadows */
        .block-container {
            background-color: white !important;
            padding: 2rem;
            border-radius: 0px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Custom CSS for styling
st.markdown(
    """
    <style>
        /* General Styles */
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f8f9fa;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }


        /* Header Section */
        .header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 20px;
            background: white;
            border-bottom: 2px solid #f0f0f0;
        }

        /* Logo and Image Container */
        .logo-container {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .logo-container img {
            height: 30px;
            width: auto;
        }

        /* Updated Logo Styles */
        .header .logo {
            font-size: 20px;
            font-weight: 800;
            color: transparent;
            background: linear-gradient(135deg, #2C3E50 0%, #3498DB 100%);
            background-clip: text;
            -webkit-background-clip: text;
            position: relative;
            letter-spacing: -0.5px;
            padding: 5px 0;
            transition: all 0.3s ease;
        }

        .header .logo::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 2px;
            background: linear-gradient(90deg, #3498DB 0%, rgba(52,152,219,0) 80%);
            opacity: 0.7;
            transition: all 0.3s ease;
        }

        .header .logo:hover {
            letter-spacing: 0px;
        }

        .header .logo:hover::after {
            opacity: 1;
            background: linear-gradient(90deg, #3498DB 0%, #2C3E50 80%);
        }

        /* Search Box */
        .search-container {
            flex: 1;
            margin: 0 20px;
            max-width: 600px;
        }

        .dropdown-input {
            width: 100%;
            padding: 10px;
            font-size: 14px;
            border: 1px solid #AAB7C4;
            border-radius: 6px;
            background: #F0F4F8;
            color: #2C3E50;
            outline: none;
        }

        .dropdown-input:focus {
            border-color: #3498DB;
            box-shadow: 0 0 5px rgba(52, 152, 219, 0.5);
        }

        .dropdown-list {
            position: absolute;
            width: 100%;
            background: white;
            border: 1px solid #AAB7C4;
            border-top: none;
            border-radius: 6px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            display: none;
            max-height: 200px;
            overflow-y: auto;
            z-index: 10;
        }

        .dropdown-item {
            padding: 10px;
            font-size: 14px;
            color: #2C3E50;
            cursor: pointer;
            transition: background 0.2s;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .dropdown-item:hover {
            background: #B0C4DE;
            color: black;
        }

        /* Top Buttons */
        .top-buttons {
            display: flex;
            gap: 10px;
        }

        .top-buttons .btn {
            border-radius: 6px;
            font-size: 14px;
            padding: 10px 20px;
            color: white;
            border: none;
            display: flex;
            align-items: center;
        }

        .top-buttons .btn i {
            margin-right: 8px;
        }

        .top-buttons .btn.btn-primary {
            background: linear-gradient(135deg, #3498DB, #2980B9);
        }

        .top-buttons .btn.btn-secondary {
            background: linear-gradient(135deg, #6C5CE7, #8E44AD);
        }

        .top-buttons .btn.btn-info {
            background: linear-gradient(135deg, #00CEC9, #00B894);
        }

        .top-buttons .btn.btn-success {
            background: linear-gradient(135deg, #00B894, #55EFC4);
        }

        .top-buttons .btn.btn-warning {
            background: linear-gradient(135deg, #FDCB6E, #E17055);
        }

        .top-buttons .btn.btn-danger {
            background: linear-gradient(135deg, #E74C3C, #C0392B);
        }

        /* Info Box Section */
        .info-box {
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.12);
            margin-bottom: 20px;
        }

        .info-box h2 {
            font-size: 28px;
            font-weight: 700;
            color: #102A43;
            margin: 0 0 15px;
        }

        .info-box p {
            font-size: 16px;
            color: #34495E;
            margin: 0 0 20px;
            line-height: 1.6;
        }

        .info-box .btn-paper {
            display: inline-flex;
            align-items: center;
            padding: 12px 24px;
            font-size: 15px;
            font-weight: 600;
            color: white;
            background: linear-gradient(135deg, #00CEC9, #00B894);
            border: none;
            border-radius: 8px;
            text-decoration: none;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            gap: 10px;
            box-shadow: 0 2px 8px rgba(0, 206, 201, 0.2);
            position: relative;
            overflow: hidden;
        }

        .info-box .btn-paper::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(
                120deg,
                transparent,
                rgba(255, 255, 255, 0.2),
                transparent
            );
            transition: all 0.6s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .info-box .btn-paper:hover {
            background: linear-gradient(135deg, #00B894, #00CEC9);
            box-shadow: 0 4px 12px rgba(0, 206, 201, 0.3);
            transform: translateY(-1px);
        }

        .info-box .btn-paper:hover::before {
            left: 100%;
        }

        .info-box .btn-paper i:first-child {
            font-size: 16px;
        }

        .info-box .btn-paper i:last-child {
            font-size: 12px;
            opacity: 0.8;
        }

        /* Table Section */
        .table-responsive {
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            background: white;
            margin-top: 20px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th {
            background: linear-gradient(135deg, #3498DB, #2980B9);
            color: white !important;
            text-align: center;
            padding: 18px !important;
            font-weight: 600;
            font-size: 15px;
            border-bottom: 2px solid #2980B9;
        }

        td {
            padding: 16px !important;
            border: 1px solid #E0E0E0;
            text-align: center;
            font-size: 14px;
            color: #333;
            background-color: #F8FAFC;
        }

        tbody tr:nth-child(odd) {
            background-color: #EAF0F6;
        }

        tbody tr:nth-child(even) {
            background-color: #DCE7F3;
        }

        tbody tr:hover {
            background-color: #B0C4DE !important;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        tbody tr:hover td {
            color: black;
        }

        /* Left-align specific columns */
        td.left-align {
            text-align: left;
        }

        /* Tooltip Styles */
        .tooltip {
            position: relative;
            display: inline-block;
            cursor: pointer;
        }

        .tooltip .tooltiptext {
            visibility: hidden;
            width: 200px;
            background-color: #555;
            color: #fff;
            text-align: center;
            border-radius: 6px;
            padding: 5px;
            position: absolute;
            z-index: 1;
            bottom: 125%;
            left: 50%;
            margin-left: -100px;
            opacity: 0;
            transition: opacity 0.3s;
        }

        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main Container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Header Section
st.markdown(
    """
    <div class="header">
        <div class="logo-container">
            <img src="https://darkblue-crab-477500.hostingersite.com/icon.png" alt="Logo Image">
            <div class="logo">Nomological Network</div>
        </div>
        <div class="search-container">
            <div class="dropdown">
                <input type="text" id="matrix-search" class="dropdown-input" placeholder="Select a matrix..." onkeyup="filterDropdown()" onclick="toggleDropdown()">
                <div class="dropdown-list" id="dropdown-options">
                    <div class="dropdown-item" onclick="selectOption(this)" title="Behavioral Medicine: PCA with Promax; NIH PROMIS-optimized dimensionality; Cutoff: 0.55">Behavioral Medicine: PCA with Promax; NIH PROMIS-optimized dimensionality; Cutoff: 0.55</div>
                    <div class="dropdown-item" onclick="selectOption(this)" title="Cognitive Functioning: EFA with Varimax; Psychological Scale Analysis; Cutoff: 0.60">Cognitive Functioning: EFA with Varimax; Psychological Scale Analysis; Cutoff: 0.60</div>
                    <div class="dropdown-item" onclick="selectOption(this)" title="Physical Health: Factor Analysis with Oblimin; NIH Health Scale; Cutoff: 0.50">Physical Health: Factor Analysis with Oblimin; NIH Health Scale; Cutoff: 0.50</div>
                    <div class="dropdown-item" onclick="selectOption(this)" title="Mental Wellness: Promax Rotation; Depression & Anxiety Scale; Cutoff: 0.65">Mental Wellness: Promax Rotation; Depression & Anxiety Scale; Cutoff: 0.65</div>
                </div>
            </div>
        </div>
        <div class="top-buttons">
            <button class="btn btn-primary"><i class="fas fa-home"></i> <span>Home</span></button>
            <button class="btn btn-secondary"><i class="fas fa-chart-bar"></i> <span>Visualize</span></button>
            <button class="btn btn-info"><i class="fas fa-search"></i> <span>Explore</span></button>
            <button class="btn btn-success"><i class="fas fa-table"></i> <span>Explore Factor</span></button>
            <button class="btn btn-warning"><i class="fas fa-file-alt"></i> <span>Implicit Definition</span></button>
            <button class="btn btn-danger"><i class="fas fa-info-circle"></i> <span>About Us</span></button>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Main Content Section
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Info Box Section
st.markdown(
    """
    <section class="info-box">
        <h2>Analysis of Latent Indicators to Generate Nomological Structures (ALIGNS)</h2>
        <p>This matrix is the result of the to date most extensive language model for psychometric indicators (questionnaire items). It is designed to work across academic disciplines, but here demonstrated on Behavioral Medicine and Information Systems indicators. It was in the final analysis optimized against the NIH PROMIS item banks.</p>
        <a href="#" class="btn-paper">
            <i class="fas fa-file-contract"></i> 
            <span>View Paper Preprint</span>
            <i class="fas fa-arrow-up-right-from-square"></i>
        </a>
    </section>
    """,
    unsafe_allow_html=True,
)

# Table Section
data = {
    "Row ID": [1, 2, 3, 4, 5, 6, 7, 8],
    "Item DB": ["CatalogueM", "CatalogueM", "NHKidsI", "NHKidsI", "CatalogueM", "NHKidsI", "HealthEval", "MentalCheck"],
    "Variable ID": [151, 153, 58, 102, 205, 85, 99, 122],
    "Variable Name": [
        "Mood And Feelings Questionnaire",
        "Mood and Feelings Questionnaire (Short)",
        "PROMIS Sleep Disturbance",
        "PROMIS Anxiety",
        "Sleep Perception Index",
        "PROMIS Depression",
        "General Wellness Survey",
        "Depression Screening",
    ],
    "Item ID": [1560, 2600, 5, 10, 220, 17, 52, 45],
    "Item Text": [
        "I felt miserable or unhappy",
        "I felt miserable or unhappy",
        "My sleep was restless",
        "I felt anxious without reason",
        "Daily stress impacts my well-being",
        "I had trouble feeling happy",
        "My mood fluctuates frequently",
        "I often feel hopeless",
    ],
    "URL": ["#", "#", "#", "#", "#", "#", "#", "#"],
    "Dim 1": [1.4457, 1.4157, 1.3559, 1.3723, 1.4021, 1.6151, 1.5592, 1.4055],
}

df = pd.DataFrame(data)

st.markdown('<section class="table-responsive">', unsafe_allow_html=True)
st.table(df)
st.markdown("</section>", unsafe_allow_html=True)

# Close Main Content and Main Container
st.markdown("</div></div>", unsafe_allow_html=True)


# JavaScript for Dropdown Functionality
st.markdown(
    """
    <script>
        // Dropdown Functionality
        function toggleDropdown() {
            document.getElementById("dropdown-options").style.display = "block";
        }

        function filterDropdown() {
            let input = document.getElementById("matrix-search").value.toLowerCase();
            let options = document.querySelectorAll(".dropdown-item");

            options.forEach(option => {
                let text = option.innerText.toLowerCase();
                if (text.includes(input)) {
                    option.style.display = "block";
                } else {
                    option.style.display = "none";
                }
            });
        }

        function selectOption(element) {
            document.getElementById("matrix-search").value = element.innerText;
            document.getElementById("dropdown-options").style.display = "none";
        }

        // Close dropdown when clicking outside
        document.addEventListener("click", function (event) {
            let dropdown = document.querySelector(".dropdown");
            if (!dropdown.contains(event.target)) {
                document.getElementById("dropdown-options").style.display = "none";
            }
        });

        // Tooltip Functionality
        document.querySelectorAll('.tooltip').forEach(element => {
            element.addEventListener('mouseover', function () {
                this.querySelector('.tooltiptext').style.visibility = 'visible';
                this.querySelector('.tooltiptext').style.opacity = '1';
            });
            element.addEventListener('mouseout', function () {
                this.querySelector('.tooltiptext').style.visibility = 'hidden';
                this.querySelector('.tooltiptext').style.opacity = '0';
            });
        });
    </script>
    """,
    unsafe_allow_html=True,
)