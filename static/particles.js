// ===== PARTICLE ANIMATION SYSTEM =====
const canvas = document.getElementById('particleCanvas');
const ctx = canvas.getContext('2d');

let width, height, particles, mouse;

function init() {
    resize();
    mouse = { x: -1000, y: -1000 };
    particles = [];

    const count = Math.floor((width * height) / 8000);
    for (let i = 0; i < count; i++) {
        particles.push({
            x: Math.random() * width,
            y: Math.random() * height,
            vx: (Math.random() - 0.5) * 0.4,
            vy: (Math.random() - 0.5) * 0.4,
            r: Math.random() * 2 + 0.5,
            color: ['#4f8fff', '#a855f7', '#2dd4bf', '#f472b6'][Math.floor(Math.random() * 4)],
            alpha: Math.random() * 0.5 + 0.15,
            pulse: Math.random() * Math.PI * 2,
            pulseSpeed: Math.random() * 0.02 + 0.005,
        });
    }
}

function resize() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
}

function drawParticle(p) {
    p.pulse += p.pulseSpeed;
    const glowAlpha = p.alpha + Math.sin(p.pulse) * 0.1;

    ctx.beginPath();
    ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
    ctx.fillStyle = p.color;
    ctx.globalAlpha = Math.max(0, glowAlpha);
    ctx.fill();

    // glow
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.r * 3, 0, Math.PI * 2);
    const grad = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.r * 3);
    grad.addColorStop(0, p.color);
    grad.addColorStop(1, 'transparent');
    ctx.fillStyle = grad;
    ctx.globalAlpha = glowAlpha * 0.3;
    ctx.fill();
    ctx.globalAlpha = 1;
}

function connectParticles() {
    const maxDist = 120;
    for (let i = 0; i < particles.length; i++) {
        for (let j = i + 1; j < particles.length; j++) {
            const dx = particles[i].x - particles[j].x;
            const dy = particles[i].y - particles[j].y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            if (dist < maxDist) {
                ctx.beginPath();
                ctx.moveTo(particles[i].x, particles[i].y);
                ctx.lineTo(particles[j].x, particles[j].y);
                ctx.strokeStyle = particles[i].color;
                ctx.globalAlpha = (1 - dist / maxDist) * 0.08;
                ctx.lineWidth = 0.5;
                ctx.stroke();
                ctx.globalAlpha = 1;
            }
        }
    }
}

function mouseInteract(p) {
    const dx = p.x - mouse.x;
    const dy = p.y - mouse.y;
    const dist = Math.sqrt(dx * dx + dy * dy);
    const radius = 150;
    if (dist < radius) {
        const force = (radius - dist) / radius;
        p.vx += (dx / dist) * force * 0.3;
        p.vy += (dy / dist) * force * 0.3;
    }
}

function animate() {
    ctx.clearRect(0, 0, width, height);

    for (const p of particles) {
        mouseInteract(p);

        p.x += p.vx;
        p.y += p.vy;

        // damping
        p.vx *= 0.99;
        p.vy *= 0.99;

        // wrap
        if (p.x < -10) p.x = width + 10;
        if (p.x > width + 10) p.x = -10;
        if (p.y < -10) p.y = height + 10;
        if (p.y > height + 10) p.y = -10;

        drawParticle(p);
    }

    connectParticles();
    requestAnimationFrame(animate);
}

window.addEventListener('resize', () => { resize(); });

window.addEventListener('mousemove', (e) => {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
});

window.addEventListener('mouseout', () => {
    mouse.x = -1000;
    mouse.y = -1000;
});

init();
animate();
