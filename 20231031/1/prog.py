class Omnibus:
	all_attrs = dict()

	def __init__(self):
		object.__setattr__(self, "attrs", set())

	def __getattr__(self, attr):
		if attr in Omnibus.all_attrs:
			return Omnibus.all_attrs[attr]
		else:
			return 0

	def __setattr__(self, attr, value):
		if attr == "attrs":
			object.__setattr__(self, attrs, set())
		if attr not in self.attrs:
			self.attrs.add(attr)

			if not Omnibus.all_attrs.get(attr):
				Omnibus.all_attrs[attr] = 1
			else:
				Omnibus.all_attrs[attr] += 1


	def __delattr__(self, attr):
		if attr in self.attrs:
			self.attrs.remove(attr)
			Omnibus.all_attrs[attr] -= 1

import sys
exec(sys.stdin.read())