label christysinisterplanintro:
    hide screen freeroamhud with None
    Jimmy "Fuck, I'm sweating like a pig."
    Jimmy "Maybe a shower can help..."
    stop music
    scene boyslockerbathroom with fade
    "{i}As [player_name] started showering under the warm water, his eyes closed for a while.{/i}"
    play sound "audio/sfx/fewmomentslater.ogg"
    scene fewmomentslater with fade
    $ renpy.pause()
    scene boyslockerbathroom with fade
    show christy towel sinister with dissolve
    "{i}Suddenly, the sound of steps alerts him and when he turns, he sees Christy wearing only a towel.{/i}" 
    "{i}She looks at him with a sinister smile.{/i}"
    play music MUSIC_CHRISTY_THEME
    Christy "Well, well, well. What do we have here?"
    Jimmy "This is the boys bathroom."
    Jimmy "But, I believe you already know that."
    play sound "audio/sfx/giggle01.ogg"
    Christy "You know, I gotta give it to you."
    play sound "audio/sfx/laugh01.ogg"
    Christy laugh "You got big balls, both literally and figuratively. Ha, ha!"
    Christy "And you want to show your little [roommate_female] how to stand up to me."
    Christy "Cassidy rejected my orders earlier today and told me she'd never play along with my bullshit anymore. Her words."
    Christy "I respect that, you know?"
    play sound "audio/sfx/hum01.ogg"
    Christy mad "But, I know what you did with the extinguisher that day."
    Christy "I get that you want to help her."
    Christy "However, you should know that even if she tries to hide it..."
    Christy "Her deepest desire is to become someone like me."
    Jimmy "A self-entitled bitch? That's a really low bar."
    Christy "Funny... Tell, me, new guy, do you like what you see?"
    "{i}[player_name] didn't say anything, but Christy saw the desire in his eyes.{/i}"
    Christy "I thought so..."
    call christy_blowjob_scene from _call_christy_blowjob_scene
    scene boyslockerbathroom with fade
    Jimmy "What the fuck was that?"
    Jimmy "Fucking cheerleaders..."
    scene fewmomentslater with fade
    call nexttime from _call_nexttime_48
    $ quests.christyPlan = SATISFIED
    $ quests.cassidyFirstFuck = SATISFIED
    $ gotoscene('schoolgymboyslockers', transition=fade)
