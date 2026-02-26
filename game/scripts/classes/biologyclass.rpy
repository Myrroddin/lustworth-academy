label biologyclass:
    hide screen freeroamhud
    scene biologyclassroomfallday with fade
    call subject('biology') from _call_subject_2
    $ gotoscene('mainbuildinglefthallway', transition=fade)

label biology_minigame:
    $ lesson = classes['biology'].lesson
    Developer "{i}Minigame coming soon!{/i}"
    return True

## Lesson failed
label biology_failintro:
    DrLed "Since last lesson proved to be such a struggle for many of you, we are going to repeat the dissection."
    DrLed "Please, get out your scalpels."
    return

label biology_failoutro:
    show drled with dissolve
    DrLed "Hmm, no, that just won't do."
    DrLed "We'll repeat this exercise next class, then."
    return

## Lesson 1
label biology_lesson1intro:
    show drled with dissolve
    DrLed "Welcome, welcome, students."
    DrLed "As you can see, I've been busy preparing the lesson."
    DrLed "And to answer what I'm sure many of you are wondering - this is {i}not{/i} human blood."
    __("Da fuq?")
    DrLed "Today, we are going to start with the basics."
    DrLed "By the time you finish my class - {i}if{/i} you finish my class..."
    DrLed "You'll be able to perform surgery, even if you don't have a license."
    DrLed "Don't worry, I don't have one either."
    DrLed "That's just how medicine works."
    DrLed "Anyone can be a doctor if they want it enough."
    __("This guy's a psycho.")
    DrLed "Well, let's begin with the first lesson."
    return

label biology_lesson1outro:
    DrLed "Nice work, Mr. [player_surname]!"
    DrLed "One of these days I might call you to be my assistant in the operating room."
    Jimmy "Um... Sure..."
    DrLed "Well, that's it for today, folks."
    return

## Lesson 2
label biology_lesson2intro:
    return

label biology_lesson2outro:
    return
