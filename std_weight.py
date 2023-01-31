def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = int(input("키를 입력하세요: "))
gender = input("성별을 입력하세요: ")
weight = round(std_weight(height / 100, gender))
print(f"키 {height}cm {gender}의 표준 체중은 {weight}kg입니다.")

