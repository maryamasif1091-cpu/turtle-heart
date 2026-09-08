import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Heart", layout="centered")

# Hide default Streamlit padding & header
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

# HTML/Canvas animation with changing background colors
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
            transition: background-color 2s ease;
        }
        canvas {
            background-color: transparent;
        }
    </style>
</head>
<body>
    <canvas id="heartCanvas"></canvas>
    <script>
        const canvas = document.getElementById("heartCanvas");
        const ctx = canvas.getContext("2d");

        const size = 350;
        canvas.width = size;
        canvas.height = size;

        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const scale = 10;

        const colors = ["red", "orange", "yellow", "green", "cyan", "lime", "purple", "pink"];
        const bgColors = ["black", "lightblue", "cyan", "darkblue", "purple", "midnightblue"];
        let bgIndex = 0;
        let i = 0;

        // Background color changing interval
        setInterval(() => {
            bgIndex = (bgIndex + 1) % bgColors.length;
            document.body.style.backgroundColor = bgColors[bgIndex];
        }, 3000);

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
            ctx.lineWidth = 1.5;
            ctx.stroke();

            i++;
            setTimeout(drawNextPoint, 30);
        }

        drawNextPoint();
    </script>
</body>
</html>
"""

components.html(heart_html, height=450)
