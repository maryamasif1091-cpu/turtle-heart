import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Heart", layout="wide")

# CSS to hide Streamlit header and padding
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
    </style>
""", unsafe_allow_html=True)

# Full screen canvas without text
heart_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            margin: 0;
            background-color: black;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
        }
        canvas {
            background-color: black;
        }
    </style>
</head>
<body>
    <canvas id="heartCanvas"></canvas>
    <script>
        const canvas = document.getElementById("heartCanvas");
        const ctx = canvas.getContext("2d");

        // Bigger size for desktop & mobile screen
        const size = Math.min(window.innerWidth, 600);
        canvas.width = size;
        canvas.height = size;

        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const scale = size / 22; // Scale increased for larger heart

        const colors = ["red", "orange", "yellow", "green", "cyan", "lime", "purple", "pink"];
        let i = 0;

        function drawNextPoint() {
            if (i >= 120) return;

            let angle = i * (Math.PI * 2) / 120;
            let x = 16 * Math.pow(Math.sin(angle), 3) * scale;
            let y = -(13 * Math.cos(angle) - 5 * Math.cos(2 * angle) - 2 * Math.cos(3 * angle) - Math.cos(4 * angle)) * scale;

            let color = colors[Math.floor(Math.random() * colors.length)];

            ctx.beginPath();
            ctx.moveTo(centerX, centerY - 20);
            ctx.lineTo(centerX + x, centerY + y);
            ctx.strokeStyle = color;
            ctx.lineWidth = 2;
            ctx.stroke();

            i++;
            setTimeout(drawNextPoint, 30);
        }

        drawNextPoint();
    </script>
</body>
</html>
"""

components.html(heart_html, height=650)
