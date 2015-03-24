formatter = "%r %r %r %r" #  %r instead of %s gives raw variable that includes quotes

print formatter % (1, 2, 3, 4,)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter) # this just outputs what the variable formatter contains
print formatter % (
	"I had this thing.", # comma appends
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)