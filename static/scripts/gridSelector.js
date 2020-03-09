var counter = 0;

document.getElementById("myCanvas").addEventListener('mousedown', logDown);

function logDown(e){

    //Finds the exact coordinate of the mouse click
    var rect = document.getElementById("myCanvas").getBoundingClientRect();
    var xValue = e.clientX - rect.left;
    var yValue = e.clientY - rect.top;
    
    //Decides which tile is being clicked.
    xValue = Math.floor(xValue/96);
    yValue = Math.floor(yValue/90);

    counter++;
    sequence = document.getElementById("gridSequence").value;
    document.getElementById("gridSequence").value = sequence + xValue + yValue + " ";
    document.getElementById("numberinsequence").innerText = "Number of Tiles Clicked : " + counter.toString();
    document.getElementById("tilesClicked").value = counter.toString();
};

//Function that resets the sequence
function clearSequence(){
    document.getElementById("gridSequence").value = "";
    counter = 0;
    document.getElementById("numberinsequence").innerText = "Number of Tiles Clicked : " + counter.toString();
    document.getElementById("tilesClicked").value = counter.toString();
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


