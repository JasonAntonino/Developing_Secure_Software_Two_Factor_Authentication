function image1() {
    // document.getElementById("imageToUse").setAttribute("value", "1");
    document.getElementById("imageToUse").value = "0";
    document.getElementById("imageboxcontent").src = "../static/images/cat.jpg";

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
};

function image2() {
    // document.getElementById("imageToUse").setAttribute("value", "2");
    document.getElementById("imageToUse").value = "1";
    document.getElementById("imageboxcontent").src = "../static/images/duck.jpg";
    
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
};

function image3() {
    // document.getElementById("imageToUse").setAttribute("value", "3");
    document.getElementById("imageToUse").value = "2";
    document.getElementById("imageboxcontent").src = "../static/images/tiger.jpg";
    
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
};