execute:compile
	java -cp bin aplicacion.Principal
compile:clear
	mkdir -p bin
	find . -name *.java | xargs javac -cp "lib/*:bin" -d bin
clear:
	rm -rf html
	rm -rf bin/*