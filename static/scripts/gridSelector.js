function gridSelector(identifier){
    sequence = document.getElementById("gridSequence").value;
    document.getElementById("gridSequence").value = sequence + identifier + " ";
    document.getElementById("sequencetext").innerHTML = document.getElementById("gridSequence").value;
    // alert(document.getElementById("gridSequence").value);
    // alert(document.getElementById("sequencetext").innerHTML);
};