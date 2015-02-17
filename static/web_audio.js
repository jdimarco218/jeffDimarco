var oscOn = function(){
    //oscillator = context.createOscillator(),
    //oscillator.type = 2;
    //oscillator.frequency.value = 200;
    //gainNode = context.createGainNode();
    //oscillator.connect(gainNode);
    //gainNode.connect(context.destination);
    //gainNode.gain.value = 1;
    //oscillator.noteOn(0);
  
    oscillator = context.createOscillator();
    oscillator.frequency.value = 200;
    oscillator.connect(context.destination);
    oscillator.start(0); 
};

var buttonClickResult = function (){
    var button = document.getElementById('audio_toggle_button');
    button.onclick = function buttonClicked(){
        if(button.className=="off"){
            window.alert("Starting oscillator!");
            button.className = "on";
            button.src = stopImage;
            oscOn();
        } else if(button.className == "on"){
            window.alert("Stopping oscillator!");
            button.className = "off";
            button.src = playImage;
            oscillator.disconnect();
        }
    }
};

buttonClickResult();

if('webkitAudioContext' in window) {
    window.alert("We have webkitAudioContext!");
    var context = new webkitAudioContext();
}else{
    window.alert("We DON'T have webkitAudioContext!");
}
//var context = new webkitAudioContext();

