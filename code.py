import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Heart", layout="centered")

# Hide Streamlit header & margins
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

# HTML/Canvas code with 3 dark backgrounds & glowing neon heart
heart_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            margin: 0;
            background-color: #000000;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
            transition: background-color 2.5s ease;
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

        // Ultra-bright neon palette for high contrast
        const neonColors = [
            "#FF007F", "#00F0FF", "#00FF66", "#FF00F5", 
            "#FFFF00", "#FF5F00", "#9D00FF", "#00FFA6"
        ];
        
        // Strictly 3 dark background colors
        const bgColors = ["#000000", "#1A0033", "#000524"]; 
        let bgIndex = 0;
        let i = 0;

        // Background transition loop
        setInterval(() => {
            bgIndex = (bgIndex + 1) % bgColors.length;
            document.body.style.backgroundColor = bgColors[bgIndex];
        }, 3500);

        function drawNextPoint() {
            if (i >= 120) return;

            let angle = i * (Math.PI * 2) / 120;
            let x = 16 * Math.pow(Math.sin(angle), 3) * scale;
            let y = -(13 * Math.cos(angle) - 5 * Math.cos(2 * angle) - 2 * Math.cos(3 * angle) - Math.cos(4 * angle)) * scale;

            let color = neonColors[Math.floor(Math.random() * neonColors.length)];

            // Interactive glowing lines effect
            ctx.shadowBlur = 8;
            ctx.shadowColor = color;

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

components.html(heart_html, height=450)
