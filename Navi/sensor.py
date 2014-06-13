__author__ = 'dmicomrt'

foo = [{"id":1, "od":2},{"id":3, "od":4}]
print foo[0]['id']
fo = {"id":5, "od":6}
foo.append(fo)
print foo[2]["od"]
fo = {"id":1, "od":2}
#foo.remove(fo)
foo.pop(0)
print foo[0]['id']
foo[0]["run"] = 5
print foo[0]["run"]
