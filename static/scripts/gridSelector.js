var counter = 0;

document.getElementById("myCanvas").addEventListener('mousedown', logDown);

//Function that calculates the sequence (which tile is clicked) and displays the order in which the tiles are clicked
function logDown(e){
    counter++;
    var canvas = document.getElementById("myCanvas");
    var ctx = canvas.getContext("2d");
    
    //Sets the font and font colour
    ctx.font = "16px Arial";
    ctx.fillStyle = "white";
    ctx.strokeStyle = 'black';
    ctx.lineWidth = 4;
    
    
    
    //Finds the exact coordinate of the mouse click
    var rect = document.getElementById("myCanvas").getBoundingClientRect();
    var xValue = e.clientX - rect.left;
    var yValue = e.clientY - rect.top;
    
    //Adds the click counter on the canvas
    ctx.strokeText(counter.toString(), xValue, yValue);
    ctx.fillText(counter.toString(), xValue, yValue);

    //Decides which tile is being clicked.
    xValue = Math.floor(xValue/96);
    yValue = Math.floor(yValue/90);

    
    sequence = document.getElementById("gridSequence").value;
    document.getElementById("gridSequence").value = sequence + xValue + yValue + " ";
    document.getElementById("numberinsequence").innerText = "Number of Tiles Clicked : " + counter.toString();
    document.getElementById("tilesClicked").value = counter.toString();
    
    if (counter == 10){
        document.getElementById("myCanvas").removeEventListener('mousedown', logDown);
    }
};

//Function that resets the sequence
function clearSequence(){
    document.getElementById("myCanvas").addEventListener('mousedown', logDown);
    document.getElementById("gridSequence").value = "";
    counter = 0;
    document.getElementById("numberinsequence").innerText = "Number of Tiles Clicked : " + counter.toString();
    document.getElementById("tilesClicked").value = counter.toString();

    //Clears everything from the canvas and redraws the image and the grid.
    var c=document.getElementById("myCanvas");
    var ctx=c.getContext("2d");
    var img = document.getElementById("imageboxcontent");
    ctx.clearRect(0,0, 960, 540);
    ctx.drawImage(img,0,0, 960, 540);

    // Iterates through column
    for (var i = 0; i < 7; i++){
        //Iterates through rows
        for(var j = 0; j < 11; j++){
            ctx.strokeStyle = "#FF0000";
            ctx.strokeRect((-96 + 96*(j+1)) , (-90 + 90*(i+1)) , 96*(j+1) , 90*(i+1));
        }
    }
}


////Old grid selector (used for image map implementation)
// function gridSelector(identifier){
//     counter++;
//     sequence = document.getElementById("gridSequence").value;
//     document.getElementById("gridSequence").value = sequence + identifier + " ";
//     // document.getElementById("sequencetext").innerHTML = document.getElementById("gridSequence").value;
//     document.getElementById("numberinsequence").innerText = "Number of Tiles Clicked : " + counter.toString();
//     document.getElementById("tilesClicked").value = counter.toString();
//     // alert(document.getElementById("gridSequence").value);
//     // alert(document.getElementById("sequencetext").innerHTML);
// };


