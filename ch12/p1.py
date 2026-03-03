# p1.py

## 이스케이프(escape)문자
# "\n" = new line
# "\t" = tab
# "\b" = backspace
# "\'" = 작은따옴표 표시
# "\"" = 큰따옴표 표시
# "\\" = 역슬래시
# "\r" = carriage return(커서를 현재 줄 가장 앞으로 이동)
print("hello\t \"great\" world!", end="\n")
print(" \bthanks!", end='\n')


path = 'ch12/계좌1.txt'
mode = 'w'
encoding = 'utf-8'
with open(path, mode, encoding=encoding) as f:
    f.write("김삿갓 597-89-000089\n")
    f.write("이수근 343-64-000064\n")
    f.write("박혁거세 136-97-000097\n")

mode = 'r'
buf = []
with open(path, mode, encoding=encoding) as f:
    lines = f.readlines()
    for line in lines:
        buf.append(line.split()[1])
print(buf)