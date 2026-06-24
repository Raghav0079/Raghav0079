"""
Generate living, breathing SVG sections — adapted for Raghav Mishra.
Uses foreignObject with HTML+CSS animations.
Run once locally (or via GitHub Actions) to write the SVG files into assets/.
"""
import math


def generate_living_hero():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 280" width="100%">
<style>
  @keyframes gentleFloat {
    0%, 100% { transform: translateY(0px); }
    50%       { transform: translateY(-8px); }
  }
  @keyframes breathe {
    0%, 100% { opacity: 0.7; }
    50%       { opacity: 1; }
  }
  @keyframes slowSway {
    0%, 100% { transform: translateX(0px) translateY(0px); }
    25%       { transform: translateX(3px)  translateY(-5px); }
    75%       { transform: translateX(-3px) translateY(-3px); }
  }
  @keyframes pulseGlow {
    0%, 100% { filter: drop-shadow(0 0 8px rgba(0,212,200,0.3)); }
    50%       { filter: drop-shadow(0 0 22px rgba(0,212,200,0.65)); }
  }
  @keyframes waveFlow {
    from { transform: translateX(0); }
    to   { transform: translateX(-900px); }
  }
  @keyframes particleDrift {
    0%   { transform: translateY(0)     translateX(0);   opacity: 0; }
    10%  { opacity: 0.6; }
    90%  { opacity: 0.6; }
    100% { transform: translateY(-260px) translateX(40px); opacity: 0; }
  }
</style>
<defs>
  <linearGradient id="heroBg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"   stop-color="#010914" stop-opacity="0.97"/>
    <stop offset="100%" stop-color="#040d1e" stop-opacity="0.99"/>
  </linearGradient>
  <linearGradient id="waveGrad" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"   stop-color="#00D4C8" stop-opacity="0.07"/>
    <stop offset="100%" stop-color="#7c3aed" stop-opacity="0.03"/>
  </linearGradient>
  <linearGradient id="waveStroke" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%"   stop-color="#00D4C8" stop-opacity="0.12"/>
    <stop offset="50%"  stop-color="#a78bfa" stop-opacity="0.22"/>
    <stop offset="100%" stop-color="#00D4C8" stop-opacity="0.12"/>
  </linearGradient>
</defs>

<!-- Background -->
<rect width="900" height="280" fill="url(#heroBg)" rx="0"/>
'''
    # Wave paths
    for i, (amp, freq, dur, opacity) in enumerate([
        (12, 300, 20, 0.5), (15, 250, 15, 0.6), (10, 350, 25, 0.4)
    ]):
        d = "M -900 280 "
        y_base = 220 + i * 15
        for x in range(-900, 1801, 30):
            y  = y_base + amp * math.sin((x + i * 200) / freq * math.pi)
            y += amp * 0.3 * math.sin(x / 80 * math.pi)
            d += f"L {x} {y:.1f} "
        d += "L 1800 280 Z"
        svg += f'\n<path d="{d}" fill="url(#waveGrad)" stroke="url(#waveStroke)" stroke-width="0.8" style="animation: waveFlow {dur}s linear infinite;"/>'

    # Particles (teal/purple palette)
    particles = [
        (110,260,12,0.0),(280,270,15,1.5),(450,255,10,3.0),
        (610,265,13,4.5),(770,258,11,6.0),(190,268,14,2.0),
        (680,262,16,5.0),(380,275,9,7.0),
    ]
    colors = ['#00D4C8','#a78bfa','#c4b5fd','#7c3aed']
    for idx,(px,py,dur,delay) in enumerate(particles):
        c = colors[idx % 4]
        svg += f'\n<circle cx="{px}" cy="{py}" r="1.5" fill="{c}" style="animation: particleDrift {dur}s ease-in-out infinite {delay}s;"/>'

    svg += '''

<!-- Star dots -->
<circle cx="35"  cy="18"  r="1.1" fill="#00D4C8" opacity="0.5"/>
<circle cx="110" cy="42"  r="0.7" fill="#a78bfa"  opacity="0.4"/>
<circle cx="220" cy="12"  r="0.9" fill="#00D4C8" opacity="0.38"/>
<circle cx="580" cy="25"  r="0.8" fill="#a78bfa"  opacity="0.38"/>
<circle cx="750" cy="14"  r="1.1" fill="#00D4C8" opacity="0.42"/>
<circle cx="870" cy="20"  r="0.9" fill="#a78bfa"  opacity="0.38"/>

<!-- Living hero content -->
<foreignObject x="0" y="0" width="900" height="280">
  <div xmlns="http://www.w3.org/1999/xhtml" style="
    width:100%; height:100%;
    display:flex; flex-direction:column;
    align-items:center; justify-content:center;
    font-family:'Trebuchet MS','Arial Black',sans-serif;
    color:#fff; text-align:center;
    box-sizing:border-box; padding:20px;
  ">
    <!-- Name -->
    <div style="animation: gentleFloat 6s ease-in-out infinite; margin-bottom:8px;">
      <div style="
        font-size:58px; font-weight:900; letter-spacing:8px;
        background: linear-gradient(135deg,#dff6f5,#00D4C8,#dff6f5);
        -webkit-background-clip:text; -webkit-text-fill-color:transparent;
        background-clip:text;
        animation: pulseGlow 4s ease-in-out infinite;
      ">RAGHAV MISHRA</div>
    </div>

    <!-- Designation -->
    <div style="animation: slowSway 8s ease-in-out infinite; margin-bottom:10px;">
      <div style="
        font-size:12px; letter-spacing:7px;
        color:#00D4C8; opacity:0.85;
        font-family:'Courier New',monospace;
        animation: breathe 3s ease-in-out infinite;
      ">A I &nbsp;/&nbsp; M L &nbsp;E N G I N E E R &nbsp;—&nbsp; R E S E A R C H E R &nbsp;—&nbsp; B U I L D E R</div>
    </div>

    <!-- Roles -->
    <div style="animation: gentleFloat 7s ease-in-out infinite 1s; margin-bottom:14px;">
      <div style="
        font-size:11.5px; letter-spacing:1px;
        color:#6d8fa8; font-style:italic;
        font-family:Georgia,serif;
      ">LLM Orchestration · Agentic AI Systems · Data Engineering · Edge ML Inference</div>
    </div>

    <!-- Badge -->
    <div style="animation: slowSway 9s ease-in-out infinite 0.5s;">
      <div style="
        display:inline-block;
        background:rgba(4,15,26,0.9);
        border:1.2px solid rgba(0,212,200,0.6);
        border-radius:14px; padding:6px 20px;
        font-size:11px; letter-spacing:2.5px;
        color:#00D4C8;
        font-family:'Courier New',monospace;
        animation: breathe 5s ease-in-out infinite 1s;
      ">✦&nbsp; B.TECH (HONS.) AI &nbsp;·&nbsp; SAGE UNIVERSITY, INDORE &nbsp;✦</div>
    </div>
  </div>
</foreignObject>
</svg>'''
    return svg


def generate_living_signoff():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 220" width="100%">
<style>
  @keyframes floatUp {
    0%, 100% { transform: translateY(0); }
    50%       { transform: translateY(-6px); }
  }
  @keyframes breatheSlow {
    0%, 100% { opacity: 0.5; }
    50%       { opacity: 1;   }
  }
  @keyframes glowRotate {
    0%   { transform: rotate(0deg);   }
    100% { transform: rotate(360deg); }
  }
</style>
<defs>
  <linearGradient id="signBg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"   stop-color="#040d1e"/>
    <stop offset="100%" stop-color="#010914"/>
  </linearGradient>
  <radialGradient id="centerGlow">
    <stop offset="0%"   stop-color="#00D4C8" stop-opacity="0.06"/>
    <stop offset="100%" stop-color="#010914" stop-opacity="0"/>
  </radialGradient>
</defs>
<rect width="900" height="220" fill="url(#signBg)" rx="0"/>
<ellipse cx="450" cy="110" rx="320" ry="90" fill="url(#centerGlow)" style="animation: breatheSlow 6s ease-in-out infinite;"/>
<g style="transform-origin:450px 110px; animation: glowRotate 30s linear infinite;">
  <ellipse cx="450" cy="110" rx="280" ry="75" fill="none" stroke="#00D4C8" stroke-width="0.5" stroke-opacity="0.1" stroke-dasharray="8 12"/>
</g>
<g style="transform-origin:450px 110px; animation: glowRotate 20s linear infinite reverse;">
  <ellipse cx="450" cy="110" rx="220" ry="55" fill="none" stroke="#a78bfa" stroke-width="0.5" stroke-opacity="0.08" stroke-dasharray="5 10"/>
</g>
<foreignObject x="0" y="0" width="900" height="220">
  <div xmlns="http://www.w3.org/1999/xhtml" style="
    width:100%; height:100%;
    display:flex; flex-direction:column;
    align-items:center; justify-content:center;
    font-family:'Courier New',monospace;
    color:#fff; text-align:center;
    box-sizing:border-box; padding:20px;
  ">
    <div style="animation: floatUp 5s ease-in-out infinite; margin-bottom:6px;">
      <div style="font-size:12px; letter-spacing:2px; color:#00D4C8; animation: breatheSlow 4s ease-in-out infinite;">
        "I am not just writing code. I am encoding intelligence."
      </div>
    </div>
    <div style="animation: floatUp 6s ease-in-out infinite 0.8s; margin-bottom:6px;">
      <div style="font-size:12px; letter-spacing:2px; color:#a78bfa; animation: breatheSlow 4s ease-in-out infinite 1s;">
        "Every pipeline is a step toward understanding data at scale."
      </div>
    </div>
    <div style="animation: floatUp 7s ease-in-out infinite 1.6s; margin-bottom:16px;">
      <div style="font-size:12px; letter-spacing:2px; color:#c4b5fd; animation: breatheSlow 4s ease-in-out infinite 2s;">
        "Production deployment isn't the end. It's where learning begins."
      </div>
    </div>
    <div style="animation: floatUp 8s ease-in-out infinite 0.5s;">
      <div style="font-size:11px; letter-spacing:4px; color:#6d8fa8; font-style:italic; animation: breatheSlow 6s ease-in-out infinite;">
        From model internals to production deployment.
      </div>
    </div>
    <div style="animation: breatheSlow 8s ease-in-out infinite 2s; margin-top:12px;">
      <div style="font-size:9px; letter-spacing:2px; color:rgba(255,255,255,0.3); font-style:italic;">
        Always reading papers. Always shipping code.
      </div>
    </div>
  </div>
</foreignObject>
</svg>'''
    return svg


# ── Write all living sections ──
sections = {
    'assets/living-hero.svg':    generate_living_hero(),
    'assets/living-signoff.svg': generate_living_signoff(),
}

for path, content in sections.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated {path}")

print("All living sections generated.")
