window.addEventListener('load', function(){
    const canvas = document.getElementById('fractal');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    // Canvas Settings
    ctx.fillStyle = 'yellow';
    ctx.lineCap = 'round';
    ctx.shadowColor = 'rgba(0, 0, 0, 0.3)';
    ctx.shadoudOffsetX = 2;
    ctx.shadowOffsetY = 1;
    ctx.shadoudBlur = 2; 

    // Efect Settings
    let color = 'hsl(138, 68%, 36%)';
    let color1 = 'hsl(' + Math.random()*360 + ', 68%, 36%)';
    let size = canvas.width < canvas.height ? canvas.width * 0.3 : canvas.height * 0.3; // Responsitive rectangle
    let angle = Math.random() * 2.5 + 0.3;;
    let scale = Math.random() * 0.2 + 0.4; // Change to 0.5
    let sides = Math.floor(Math.random() * 4 + 3); // Number of principal branches
    let lineWidth = Math.floor(Math.random() * 15 + 10);

    const maxCounter = 3; // Segment divition for each branch
    const branches = 3;

    // Controls
    ctx.save();
    ctx.translate(canvas.width/2, canvas.height/2);
    ctx.scale(1, 1);
    ctx.rotate(0); // Change to 0
    
    
    function drawBranch(counter){
        if (counter > maxCounter) return;
        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.lineTo(size, 0);
        ctx.stroke();

        for (let i = 0; i < branches; i++){
            ctx.save();
            
            ctx.translate(size - (size/branches) * i , 0);
            ctx.scale(scale, scale);
            ctx.save()
            ctx.rotate(angle); //chage to 'angle'
            drawBranch(counter + 1);
            ctx.restore();

            ctx.save();
            ctx.rotate(-angle); //chage to 'angle'
            console.log(ctx.rotate)
            drawBranch(counter + 1);
            ctx.restore();

            ctx.restore();
        }
        
    }

    

    //Circular Fractal
    function drawFractal(){
        ctx.clearRect(-canvas.width, -canvas.height, canvas.width*2, canvas.height*2);
        ctx.save();
        ctx.strokeStyle = color;
        ctx.fill = color
        ctx.scale(0.8, 0.8);
        ctx.lineWidth = lineWidth;
        

        for (let i = 0; i < sides; i++){
            ctx.rotate((Math.PI * 2)/sides);  // Circle patron (Math.PI * 2)/sides
            drawBranch(0);
            
        }
        ctx.restore();
    }    
    drawFractal();
});