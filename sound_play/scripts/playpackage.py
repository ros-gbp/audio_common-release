#!/usr/bin/env python

#***********************************************************
#* Software License Agreement (BSD License)
#*
#*  Copyright (c) 2009, Willow Garage, Inc.
#*  All rights reserved.
#*
#*  Redistribution and use in source and binary forms, with or without
#*  modification, are permitted provided that the following conditions
#*  are met:
#*
#*   * Redistributions of source code must retain the above copyright
#*     notice, this list of conditions and the following disclaimer.
#*   * Redistributions in binary form must reproduce the above
#*     copyright notice, this list of conditions and the following
#*     disclaimer in the documentation and/or other materials provided
#*     with the distribution.
#*   * Neither the name of the Willow Garage nor the names of its
#*     contributors may be used to endorse or promote products derived
#*     from this software without specific prior written permission.
#*
#*  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#*  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#*  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
#*  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
#*  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
#*  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
#*  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#*  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#*  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
#*  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
#*  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#*  POSSIBILITY OF SUCH DAMAGE.
#***********************************************************

# Author: Matthias Nieuwenhuisen, Blaise Gassend


import sys

if __name__ == '__main__':
    if len(sys.argv) < 3 or len(sys.argv) > 4 or sys.argv[1] == '--help':
        print('Usage: %s package sound_to_play.(ogg|wav) [volume]' % sys.argv[0])
        print()
        print('Plays an .OGG or .WAV file. The path to the file should be relative to the package, and be valid on the computer on which sound_play is running. \n The (optional) volume parameter sets the volume for the sound as a value between 0 and 1.0, where 0 is mute.')
        exit(1)

    # Import after printing usage for speed.
    import rospy
    from sound_play.msg import SoundRequest
    from sound_play.libsoundplay import SoundClient

    rospy.init_node('play', anonymous=True)
    soundhandle = SoundClient()

    volume = float(sys.argv[3]) if len(sys.argv) == 4 else 1.0

    rospy.sleep(1)
    rospy.loginfo('Playing "%s" from pkg "%s".' % (sys.argv[2], sys.argv[1]))
    soundhandle.playWaveFromPkg(sys.argv[1], sys.argv[2], volume)
    rospy.sleep(1)
