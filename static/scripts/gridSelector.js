var counter = 0;
function gridSelector(identifier){
    counter++;
    sequence = document.getElementById("gridSequence").value;
    document.getElementById("gridSequence").value = sequence + identifier + " ";
    // document.getElementById("sequencetext").innerHTML = document.getElementById("gridSequence").value;
    document.getElementById("numberinsequence").innerText = "Number of Tiles Clicked : " + counter.toString();
    document.getElementById("tilesClicked").value = counter.toString();
    // alert(document.getElementById("gridSequence").value);
    // alert(document.getElementById("sequencetext").innerHTML);
};


function clearSequence(){
    document.getElementById("gridSequence").value = "";
    // document.getElementById("sequencetext").innerHTML = " ";
    counter = 0;
    document.getElementById("numberinsequence").innerText = "Number of Tiles Clicked : " + counter.toString();
    document.getElementById("tilesClicked").value = counter.toString();
    //alert(document.getElementById("sequencetext").innerHTML);
    //alert("sequence is cleared");
}