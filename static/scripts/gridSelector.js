function gridSelector(identifier){
    sequence = document.getElementById("gridSequence").value;
    document.getElementById("gridSequence").value = sequence + identifier + " ";

    alert(document.getElementById("gridSequence").value);
}