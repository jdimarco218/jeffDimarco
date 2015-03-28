#!/bin/bash
for i in {%+1,%+6,%+13,%+6,%-4,%-9,%-7,%-11,%-2,%-7,%+0,%-4,%+3,%+0,%+6};do play -qn synth 2 pluck $i& sleep .25; done