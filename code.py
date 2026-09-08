import streamlit as st
import streamlit.components.v1 as components
import random

# Streamlit Page Config - Keep clean layout
st.set_page_config(page_title="Cardioid Heart", layout="wide")

# CSS to hide standard Streamlit elements
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding: 0rem;
        }
    </style>
""", unsafe_allow_html=True)

# Full screen HTML/Canvas components for heart and background
heart_and_bg_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            background-color: black; /* Initial background */
        }
        #canvasContainer {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            height: 100%;
            transition: background-color 2s; /* Smooth background change */
        }
        canvas {
            display: block;
        }
    </style>
</head>
<body>
    <div id="canvasContainer">
        <canvas id="heartCanvas"></canvas>
    </div>
    <script>
        const container = document.getElementById('canvasContainer');
        const canvas = document.getElementById('heartCanvas');
        const ctx = canvas.getContext('2d');

        // Set optimal canvas size - good fit but not too huge
        const baseSize = 400; // Size of the heart shape box
        canvas.width = baseSize + 50; // extra padding
        canvas.height = baseSize + 50;

        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const scale = baseSize / 15; // Scale for mathematical formula

        const colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33FB", "#33FFF5", "#FBFF33", "#FFA633", "#A633FF"];
        let colorIndex = 0;
        let points = [];
        let i = 0;
        const totalPoints = 180; // More points for a smoother curve

        // Generate the smoother Cardioid heart points
        for (let j = 0; j < totalPoints; j++) {
            let theta = (j / totalPoints) * (Math.PI * 2);
            // More natural cardioid heart shape formula
            let x = scale * 16 * Math.pow(Math.sin(theta), 3);
            let y = -scale * (13 * Math.cos(theta) - 5 * Math.cos(2 * theta) - 2 * Math.cos(3 * theta) - Math.cos(4 * theta));
            points.push({ x: centerX + x, y: centerY + y });
        }

        function drawFrame() {
            if (i < points.length) {
                // Clear and redraw for complete heart
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                // Draw heart lines from center (like user image but smooth)
                for (let k = 0; k <= i; k++) {
                    ctx.beginPath();
                    // Optional center circle point
                    ctx.moveTo(centerX, centerY - (scale * 2)); // slight offset from very center
                    ctx.lineTo(points[k].x, points[k].y);
                    ctx.strokeStyle = colors[(colorIndex + k) % colors.length];
                    ctx.lineWidth = 1.5;
                    ctx.stroke();
                }

                // Smoothly draw points along the curve
                ctx.beginPath();
                ctx.moveTo(points[0].x, points[0].y);
                for (let k = 1; k <= i; k++) {
                    ctx.lineTo(points[k].x, points[k].y);
                }
                ctx.strokeStyle = colors[colorIndex];
                ctx.lineWidth = 2.5;
                ctx.stroke();

                i++;
                requestAnimationFrame(drawFrame);
            }
        }

        // --- Background Color Changer Logic ---
        const bgColors = ["#000000", "#120021", "#021c1f", "#1e1e02"]; // Dark hues for better contrast
        let bgIndex = 0;
        function changeBackground() {
            container.style.backgroundColor = bgColors[bgIndex];
            bgIndex = (bgIndex + 1) % bgColors.length;
            colorIndex = (colorIndex + 1) % colors.length; // cycle line colors too
        }

        // Start animation after a short delay
        setTimeout(() => {
            drawFrame();
            setInterval(changeBackground, 4000); // Change background every 4 seconds
        }, 500);

    </script>
</body>
</html>
"""

# Render the combined heart and background component
# High height for full-screen feel without a heading
components.html(heart_and_bg_html, height=600, scrolling=False)
