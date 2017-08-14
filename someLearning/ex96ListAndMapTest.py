# -*- coding: UTF-8 -*-

states = {
	'oregon' : 'OR',
	'florida' : 'FL',
	'california' : 'CA',
	'new york' : 'NY',
	'michigan' : 'MI'
}

cities = {}

cities['CA'] = 'san francisco'
cities['MI'] = 'detroit'
cities['FL'] = 'jacksonville'
cities['NY'] = 'new york'
cities['OR'] = 'porland'

print '-' * 10
print "NY has: " , cities[states['new york']]
print "california has: " , cities[states['california']]

print '-' * 10
for state , abbrev in states.items() :
	print "%s is abbreviated %s" %(state , abbrev)

print '-' * 10
for abbrev , city in cities.items() :
	print "%s has the city %s" %(abbrev , city)

print '-' *10
state = states.get('TeXas',None)
if not state :
	print 'sorry'