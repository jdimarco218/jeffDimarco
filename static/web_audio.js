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
            window.alert("Starting oscillator2!");
            button.className = "on";
            button.src = stopImage;
            //oscOn();
            var ac = new (window.AudioContext || window.webkitAudioContext);
            // C4, E4, G4
            var freqs = [261.63, 329.63, 392.00];
            var oscs = [];
            // initialize the oscillators
            for(var i=0;i<freqs.length;i++) {
                var o = ac.createOscillator();
                o.frequency.value = freqs[i];
                o.connect(ac.destination);
                oscs.push(o);
            }
            // schedule noteOn and noteOff (deprecated: the methods will be renamed to start() and   stop() soon)
            for (i = 0; i < oscs.length; i +=1) {
                oscs[i].noteOn(0);
                oscs[i].noteOff(1);
            }
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

