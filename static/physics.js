// Initialize Matter.js for Skills Section
window.addEventListener('load', () => {
    if (typeof Matter === 'undefined') {
        console.error('Matter.js not loaded');
        return;
    }

    const container = document.getElementById('physics-container');
    if (!container) return;

    // Force the container to have explicit dimensions before reading them
    container.style.width = '100%';
    container.style.height = '500px';
    container.style.display = 'block';
    container.style.position = 'relative';
    container.style.overflow = 'hidden';

    // Use getBoundingClientRect to get accurate rendered dimensions
    const rect = container.getBoundingClientRect();
    const width  = rect.width  || container.offsetWidth  || 800;
    const height = rect.height || container.offsetHeight || 500;

    const { Engine, Render, Runner, Bodies, Composite, Mouse, MouseConstraint, Events } = Matter;

    const engine = Engine.create();
    engine.gravity.y = 1;

    const render = Render.create({
        element: container,
        engine: engine,
        options: {
            width:       width,
            height:      height,
            wireframes:  false,
            background:  'transparent',
            pixelRatio:  window.devicePixelRatio || 1
        }
    });

    // Style the canvas to fill the container exactly
    render.canvas.style.display  = 'block';
    render.canvas.style.position = 'absolute';
    render.canvas.style.top      = '0';
    render.canvas.style.left     = '0';
    render.canvas.style.width    = '100%';
    render.canvas.style.height   = '100%';

    // Walls — inset slightly so balls can't escape under the border
    const wall = { isStatic: true, render: { fillStyle: 'rgba(56,189,248,0.08)', strokeStyle: 'rgba(56,189,248,0.2)', lineWidth: 1 } };
    const ground   = Bodies.rectangle(width / 2,  height + 25, width + 50, 50,   wall);
    const leftWall = Bodies.rectangle(-25,          height / 2,  50, height + 50, wall);
    const rightWall= Bodies.rectangle(width + 25,  height / 2,  50, height + 50, wall);
    const ceiling  = Bodies.rectangle(width / 2, -25,           width + 50, 50,   wall);
    Composite.add(engine.world, [ground, leftWall, rightWall, ceiling]);

    // Parse skills
    let skills = [];
    const el = document.getElementById('skills-data');
    if (el) {
        try { skills = JSON.parse(el.textContent.trim()); } catch (e) {}
    }
    if (!skills.length) {
        skills = [
            { name: 'Python'   }, { name: 'C++'       }, { name: 'Java'      },
            { name: 'SQL'      }, { name: 'Flask'      }, { name: 'FastAPI'   },
            { name: 'Streamlit'}, { name: 'Git'        }, { name: 'GitHub'    },
            { name: 'MySQL'    }, { name: 'Firebase'   }, { name: 'Power BI'  },
            { name: 'DSA'      }, { name: 'OOP'        }, { name: 'DBMS'      },
            { name: 'OS'       }, { name: 'CN'         }
        ];
    }

    // Color palette for ball fills
    const colors = [
        '#7c3aed','#2563eb','#0891b2','#0d9488','#16a34a',
        '#ca8a04','#dc2626','#9333ea','#4f46e5','#0284c7'
    ];

    const skillBodies = [];
    skills.forEach((skill, i) => {
        const radius = Math.min(width / (skills.length * 0.9), 50);
        const xPos   = radius + Math.random() * (width  - radius * 2);
        const yPos   = -radius - i * (radius * 2.5);           // drop from above
        const color  = colors[i % colors.length];

        const body = Bodies.circle(xPos, yPos, radius, {
            restitution: 0.7,
            friction:    0.1,
            density:     0.05,
            render: {
                fillStyle:   color + 'cc',   // semi-transparent
                strokeStyle: color,
                lineWidth:   2
            }
        });
        body._skillName   = skill.name;
        body._skillRadius = radius;
        body._skillColor  = color;
        skillBodies.push(body);
    });
    Composite.add(engine.world, skillBodies);

    // Mouse drag
    const mouse = Mouse.create(render.canvas);
    const mc = MouseConstraint.create(engine, {
        mouse,
        constraint: { stiffness: 0.2, render: { visible: false } }
    });
    Composite.add(engine.world, mc);
    render.mouse = mouse;

    // Draw skill names on top of each bubble
    Events.on(render, 'afterRender', () => {
        const ctx = render.context;
        skillBodies.forEach(body => {
            if (!body._skillName) return;
            const { x, y } = body.position;
            const r = body._skillRadius;
            const name = body._skillName;
            const color = body._skillColor || '#38bdf8';

            // Outer glow ring
            ctx.beginPath();
            ctx.arc(x, y, r, 0, Math.PI * 2);
            ctx.strokeStyle = color;
            ctx.lineWidth = 2;
            ctx.shadowColor = color;
            ctx.shadowBlur = 15;
            ctx.stroke();
            ctx.shadowBlur = 0;

            // Skill name — shrink font if name is long
            const fontSize = name.length > 8 ? Math.max(9, Math.floor(r * 0.38)) : Math.floor(r * 0.42);
            ctx.font = `700 ${fontSize}px Poppins, sans-serif`;
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillStyle = '#ffffff';
            ctx.shadowColor = 'rgba(0,0,0,0.8)';
            ctx.shadowBlur = 4;
            ctx.fillText(name, x, y);
            ctx.shadowBlur = 0;
        });
    });

    Render.run(render);
    Runner.run(Runner.create(), engine);

    // Resize handler
    window.addEventListener('resize', () => {
        const nr = container.getBoundingClientRect();
        const nw = nr.width || 800;
        const nh = nr.height || 500;
        render.canvas.width  = nw;
        render.canvas.height = nh;
        render.options.width  = nw;
        render.options.height = nh;
        Matter.Body.setPosition(ground,    { x: nw / 2,  y: nh + 25   });
        Matter.Body.setPosition(rightWall, { x: nw + 25, y: nh / 2    });
        Matter.Body.setPosition(ceiling,   { x: nw / 2,  y: -25       });
        Matter.Body.setPosition(leftWall,  { x: -25,      y: nh / 2   });
    });
});
