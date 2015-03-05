//var oscOn = function(){
//    //oscillator = context.createOscillator(),
//    //oscillator.type = 2;
//    //oscillator.frequency.value = 200;
//    //gainNode = context.createGainNode();
//    //oscillator.connect(gainNode);
//    //gainNode.connect(context.destination);
//    //gainNode.gain.value = 1;
//    //oscillator.noteOn(0);
//  
//    oscillator = context.createOscillator();
//    oscillator.frequency.value = 200;
//    oscillator.connect(context.destination);
//    oscillator.start(0); 
//};
//
//var buttonClickResult = function (){
//    var button = document.getElementById('audio_toggle_button');
//    button.onclick = function buttonClicked(){
//        if(button.className=="off"){
//            window.alert("Starting oscillator2!");
//            button.className = "on";
//            button.src = stopImage;
//            //oscOn();
//            var ac = new (window.AudioContext || window.webkitAudioContext);
//            // C4, E4, G4
//            var freqs = [261.63, 329.63, 392.00];
//            var oscs = [];
//            // initialize the oscillators
//            for(var i=0;i<freqs.length;i++) {
//                var o = ac.createOscillator();
//                o.frequency.value = freqs[i];
//                o.connect(ac.destination);
//                oscs.push(o);
//            }
//            // schedule noteOn and noteOff (deprecated: the methods will be renamed to start() and   stop() soon)
//            for (i = 0; i < oscs.length; i +=1) {
//                oscs[i].noteOn(0);
//                oscs[i].noteOff(1);
//            }
//        } else if(button.className == "on"){
//            window.alert("Stopping oscillator!");
//            button.className = "off";
//            button.src = playImage;
//            oscillator.disconnect();
//        }
//    }
//};
//
//buttonClickResult();
//
//if('webkitAudioContext' in window) {
//    window.alert("We have webkitAudioContext!");
//    var context = new webkitAudioContext();
//}else{
//    window.alert("We DON'T have webkitAudioContext!");
//}
//var context = new webkitAudioContext();

// Fix up prefixing
//window.AudioContext = window.AudioContext || window.webkitAudioContext;
//var ctx = new AudioContext(), currentOsc;
//
//function startNote(e) {
//    var frq = notes[e.currentTarget.id], o = ctx.createOscillator();
//    $(e.currentTarget).attr("fill","yellow");
//    o.type = $("#waveType").val();
//    if (frq) {
//        $("#note").val(e.currentTarget.id);
//        o.frequency.value = frq;
//        o.connect(ctx.destination);
//        o.start(0);
//        currentOsc = o;
//    }
//}
//function stopNote(e) {
//    $(e.currentTarget).attr("fill","inherit");
//    currentOsc.stop(0);
//    $("#note").val("");
//}
//
//$("use").mousedown(startNote);
//$("use").mouseup(stopNote);
//
//var notes = {
//    'C0': 16.35,
//    'C#0': 17.32,
//    'Db0': 17.32,
//    'D0': 18.35,
//    'D#0': 19.45,
//    'Eb0': 19.45,
//    'E0': 20.60,
//    'F0': 21.83,
//    'F#0': 23.12,
//    'Gb0': 23.12,
//    'G0': 24.50,
//    'G#0': 25.96,
//    'Ab0': 25.96,
//    'A0': 27.50,
//    'A#0': 29.14,
//    'Bb0': 29.14,
//    'B0': 30.87,
//    'C1': 32.70,
//    'C#1': 34.65,
//    'Db1': 34.65,
//    'D1': 36.71,
//    'D#1': 38.89,
//    'Eb1': 38.89,
//    'E1': 41.20,
//    'F1': 43.65,
//    'F#1': 46.25,
//    'Gb1': 46.25,
//    'G1': 49.00,
//    'G#1': 51.91,
//    'Ab1': 51.91,
//    'A1': 55.00,
//    'A#1': 58.27,
//    'Bb1': 58.27,
//    'B1': 61.74,
//    'C2': 65.41,
//    'C#2': 69.30,
//    'Db2': 69.30,
//    'D2': 73.42,
//    'D#2': 77.78,
//    'Eb2': 77.78,
//    'E2': 82.41,
//    'F2': 87.31,
//    'F#2': 92.50,
//    'Gb2': 92.50,
//    'G2': 98.00,
//    'G#2': 103.83,
//    'Ab2': 103.83,
//    'A2': 110.00,
//    'A#2': 116.54,
//    'Bb2': 116.54,
//    'B2': 123.47,
//    'C3': 130.81,
//    'C#3': 138.59,
//    'Db3': 138.59,
//    'D3': 146.83,
//    'D#3': 155.56,
//    'Eb3': 155.56,
//    'E3': 164.81,
//    'F3': 174.61,
//    'F#3': 185.00,
//    'Gb3': 185.00,
//    'G3': 196.00,
//    'G#3': 207.65,
//    'Ab3': 207.65,
//    'A3': 220.00,
//    'A#3': 233.08,
//    'Bb3': 233.08,
//    'B3': 246.94,
//    'C4': 261.63,
//    'C#4': 277.18,
//    'Db4': 277.18,
//    'D4': 293.66,
//    'D#4': 311.13,
//    'Eb4': 311.13,
//    'E4': 329.63,
//    'F4': 349.23,
//    'F#4': 369.99,
//    'Gb4': 369.99,
//    'G4': 392.00,
//    'G#4': 415.30,
//    'Ab4': 415.30,
//    'A4': 440.00,
//    'A#4': 466.16,
//    'Bb4': 466.16,
//    'B4': 493.88,
//    'C5': 523.25,
//    'C#5': 554.37,
//    'Db5': 554.37,
//    'D5': 587.33,
//    'D#5': 622.25,
//    'Eb5': 622.25,
//    'E5': 659.26,
//    'F5': 698.46,
//    'F#5': 739.99,
//    'Gb5': 739.99,
//    'G5': 783.99,
//    'G#5': 830.61,
//    'Ab5': 830.61,
//    'A5': 880.00,
//    'A#5': 932.33,
//    'Bb5': 932.33,
//    'B5': 987.77,
//    'C6': 1046.50,
//    'C#6': 1108.73,
//    'Db6': 1108.73,
//    'D6': 1174.66,
//    'D#6': 1244.51,
//    'Eb6': 1244.51,
//    'E6': 1318.51,
//    'F6': 1396.91,
//    'F#6': 1479.98,
//    'Gb6': 1479.98,
//    'G6': 1567.98,
//    'G#6': 1661.22,
//    'Ab6': 1661.22,
//    'A6': 1760.00,
//    'A#6': 1864.66,
//    'Bb6': 1864.66,
//    'B6': 1975.53,
//    'C7': 2093.00,
//    'C#7': 2217.46,
//    'Db7': 2217.46,
//    'D7': 2349.32,
//    'D#7': 2489.02,
//    'Eb7': 2489.02,
//    'E7': 2637.02,
//    'F7': 2793.83,
//    'F#7': 2959.96,
//    'Gb7': 2959.96,
//    'G7': 3135.96,
//    'G#7': 3322.44,
//    'Ab7': 3322.44,
//    'A7': 3520.00,
//    'A#7': 3729.31,
//    'Bb7': 3729.31,
//    'B7': 3951.07,
//    'C8': 4186.01
//};

window.AudioContext = window.AudioContext || window.webkitAudioContext;
// create the audio context
var ac = typeof AudioContext !== 'undefined' ? new AudioContext : new webkitAudioContext,
  // get the current Web Audio timestamp (this is when playback should begin)
  when = ac.currentTime,
  // set the tempo
  tempo = 132,
  // initialize some vars
  sequence1,
  sequence2,
  sequence3,
  // create an array of "note strings" that can be passed to a sequence
  lead = [
    '-   e',
    'Bb3 e',
    'A3  e',
    'Bb3 e',
    'G3  e',
    'A3  e',
    'F3  e',
    'G3  e',

    'E3  e',
    'F3  e',
    'G3  e',
    'F3  e',
    'E3  e',
    'F3  e',
    'D3  q',

    '-   e',
    'Bb3 s',
    'A3  s',
    'Bb3 e',
    'G3  e',
    'A3  e',
    'G3  e',
    'F3  e',
    'G3  e',

    'E3  e',
    'F3  e',
    'G3  e',
    'F3  e',
    'E3  s',
    'F3  s',
    'E3  e',
    'D3  q'
  ],
  harmony = [
    '-   e',
    'D4  e',
    'C4  e',
    'D4  e',
    'Bb3 e',
    'C4  e',
    'A3  e',
    'Bb3 e',

    'G3  e',
    'A3  e',
    'Bb3 e',
    'A3  e',
    'G3  e',
    'A3  e',
    'F3  q',

    '-   e',
    'D4  s',
    'C4  s',
    'D4  e',
    'Bb3 e',
    'C4  e',
    'Bb3 e',
    'A3  e',
    'Bb3 e',

    'G3  e',
    'A3  e',
    'Bb3 e',
    'A3  e',
    'G3  s',
    'A3  s',
    'G3  e',
    'F3  q'
  ],
  bass = [
    'D3  q',
    '-   h',
    'D3  q',

    'A2  q',
    '-   h',
    'A2  q',

    'Bb2 q',
    '-   h',
    'Bb2 q',

    'F2  h',
    'A2  h'
  ];

// create 3 new sequences (one for lead, one for harmony, one for bass)
sequence1 = new Sequence( ac, tempo, lead );
sequence2 = new Sequence( ac, tempo, harmony );
sequence3 = new Sequence( ac, tempo, bass );

// set staccato and smoothing values for maximum coolness
sequence1.staccato = 0.55;
sequence2.staccato = 0.55;
sequence3.staccato = 0.05;
sequence3.smoothing = 0.4;

// adjust the levels so the bass and harmony aren't too loud
sequence1.gain.gain.value = 1.0;
sequence2.gain.gain.value = 0.8;
sequence3.gain.gain.value = 0.65;

// apply EQ settings
sequence1.mid.frequency.value = 800;
sequence1.mid.gain.value = 3;
sequence2.mid.frequency.value = 1200;
sequence3.mid.gain.value = 3;
sequence3.bass.gain.value = 6;
sequence3.bass.frequency.value = 80;
sequence3.mid.gain.value = -6;
sequence3.mid.frequency.value = 500;
sequence3.treble.gain.value = -2;
sequence3.treble.frequency.value = 1400;

// play
document.querySelector('#playGroove').addEventListener('click', function() {
  window.alert("Play pushed!");
  when = ac.currentTime;
  //start the lead part immediately
  sequence1.play( when );
  // delay the harmony by 16 beats
  sequence2.play( when + ( 60 / tempo ) * 16 );
  // start the bass part immediately
  sequence3.play( when );
}, false );

// pause
document.querySelector('#stopGroove').addEventListener('click', function() {
  window.alert("Stop pushed!");
  sequence1.stop();
  sequence2.stop();
  sequence3.stop();
}, false );
