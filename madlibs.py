""" This is a project used to create a Mad Libs Generator """

def madlib():
	print "Hello!"
	print "We are going to do a madlib!"
	print "Please choose from the following madlib categories:"
	print "1. Dining Room Wars"
	print "2. Happy Couple"
	answer = raw_input("Please type number: ")
	if answer == "1":
		dining()
	elif answer == "2":
		happycouple()
	else:
		print "Sorry you didn't choose one! Thanks for trying."

def dining():
	noun1 = raw_input("Please list a noun: ")
	noun2 = raw_input("Please list a noun: ")
	plural1 = raw_input("Please list a plural noun: ")
	adj1 = raw_input("Please list a adjective: ")
	adj2 = raw_input("Please list a adjective: ")
	adj3 = raw_input("Please list a adjective: ")
	noun3 = raw_input("Please list a noun: ")
	adverb1 = raw_input("Please list a adverb: ")
	plural2 = raw_input("Please list a plural noun: ")
	adj4 = raw_input("Please list a adjective: ")
	adj5 = raw_input("Please list a adjective: ")
	print "Our dining %s used to be a war %s." % (noun1, noun2)
	print "I thougt the battles about correct table %s would never end." % plural1
	print "It was us kids versus Mom, and it seemed like a fight that would last to the %s end." % adj1
	print "But tonight Dad finally declared a/an %s truce, and we negotiated a/an %s peace %s." % (adj2, adj3, noun3)
	print "Mom promised to no longer get %s upset and shoot us dirty %s and make %s remarks when we do %s things she doesn't like." % (adverb1, plural2, adj4, adj5)

def happycouple():
	adj_1 = raw_input("List adjective: ")
	noun_1 = raw_input("List noun: ")
	noun_2 = raw_input("List noun: ")
	adj_2 = raw_input("List adjective: ")
	print "We are %s to be here today with you to celebrate your %s." % (adj_1, noun_1)
	print "Although I love and support you both, let's face it."
	print "I'm really here for the %s!" % (noun_2)
	print "With my many years of wisdom, here is my best advice to pull you through the %s years ahead." % (adj_2)
madlib()