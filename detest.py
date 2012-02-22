from depy.depy import * 

novel = VisualNovel("theboywholived.db")

currentScene = novel.get_scene(novel.current_scene)

while(currentScene is not None):
	currentDialogue = currentScene.initial_dialogue
	print currentScene.setup_text + "\n"
	while(currentDialogue is not None):
		print "%s: %s" % (currentDialogue.actor.name, currentDialogue.text)
		option = "0"
		
		if (len(currentDialogue.options) > 1):
			for i in len(currentDialogue.options):
				print "%s: %s" % (i, currentDialogue.options[i].display_text)
			option = raw_input()
		else:
			print currentDialogue.options[0].display_text
			raw_input()

		choiceInd = int(option)
		userOption = currentDialogue.options[choiceInd]
		print userOption.text
		if(userOption.outcome_type == Outcome.DIALOGUE):
			currentDialogue = novel.get_dialogue(userOption.outcome_ref)
		elif (userOption.outcome_type == Outcome.SCENE):
			currentDialogue = None
			currentScene = novel.get_scene(userOption.outcome_ref)
		elif (userOption.outcome_type == Outcome.GAMEEND):
			currentDialogue = None
			currentScene = None
print "The End"
