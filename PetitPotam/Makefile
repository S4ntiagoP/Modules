BOF := PetitPotam
CC_x64 := x86_64-w64-mingw32-gcc
STRIP_x64 := x86_64-w64-mingw32-strip

all:
	$(CC_x64) -I include -o bin/$(BOF).o -c src/$(BOF).c
	$(STRIP_x64) --strip-unneeded bin/$(BOF).o

clean:
	rm ../$(BOF).o
