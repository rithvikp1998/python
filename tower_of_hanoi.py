def moveTower(height, fromPeg,withPeg, toPeg):
	if height>=1:
		moveTower(height-1,fromPeg,toPeg,withPeg)
		moveDisk(fromPeg,toPeg)
		moveTower(height-1,withPeg,fromPeg,toPeg)
def moveDisk(fp,tp):
	print('Moving disk from',fp,'to',tp)
moveTower(2,'a','b','c')
