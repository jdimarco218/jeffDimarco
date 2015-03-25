function playNoteList(ac, sequence1, sequence2, noteList, noteListBass) {

    //window.AudioContext = window.AudioContext || window.webkitAudioContext;
    // create the audio context
    //var ac = typeof AudioContext !== 'undefined' ? new AudioContext : new webkitAudioContext,
    //ac = typeof AudioContext !== 'undefined' ? new AudioContext : new webkitAudioContext,
      // get the current Web Audio timestamp (this is when playback should begin)
      var when = ac.currentTime;
      //var when = ac.currentTime,
      // set the tempo
      var tempo = 132;
      //var tempo = 132,
      // initialize some vars
      //var sequence1;
      //var sequence2;
      // create an array of "note strings" that can be passed to a sequence
    
    //sequence1.waveType = 'sine';
    //sequence2.waveType = 'sine';
    // create 3 new sequences (one for lead, one for harmony, one for bass)
    sequence1 = new Sequence( ac, tempo, noteList );
    sequence2 = new Sequence( ac, tempo, noteListBass );
    
    // set staccato and smoothing values for maximum coolness
    sequence1.staccato = 0.55;
    sequence2.staccato = 0.05;
    sequence2.smoothing = 0.4;
    
    // adjust the levels so the bass and harmony aren't too loud
    sequence1.gain.gain.value = 0.75;
    sequence2.gain.gain.value = 0.5;
    
    // apply EQ settings
    sequence1.mid.frequency.value = 500;
    sequence1.mid.gain.value = 3;
    sequence2.mid.gain.value = 0.2;
    sequence2.bass.gain.value = 6;
    sequence2.bass.frequency.value = 80;
    sequence2.mid.gain.value = 0.2;
    sequence2.mid.frequency.value = 500;
    sequence2.treble.gain.value = 0.2;
    sequence2.treble.frequency.value = 1400;

    // Wave type
    sequence1.waveType = 'triangle';
    sequence2.waveType = 'triangle';
    //sequence1.createCustomWave([-1,-0.9,-0.6,-0.3, 0, 0.3, 0.6, 0.9,1]);

    sequence1.loop = false;
    sequence1.play( when );
    sequence2.loop = false;
    sequence2.play( when );

    //useless delete lolz
    delete sequence1;
    delete sequence2;
}

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
