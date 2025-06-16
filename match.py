def match_example(point):
  match point:
    case (0, 0):
      print("origin")
    case (0, y):
      print(f"2:y={y:3}")
    case (x, 0):
      print(f"3:x={x:3d}") # 以空格補滿3位
    case (x, y):
      print(f"4:x={x:06.3f}, y={y}") # : 用來格式化數值，還不是很了解格式。
      # 06.3f -> 共6位，補0，f:小數點後佔3位
    case (x, y, z):
      print(f"5:x={x:06.3f}, y={y}, z={z:06.2f}") # : 用來格式化數值，還不是很了解格式。
      # 2f 2位以後四捨五入

a = (1.1, 1.2) # tuple
match_example(a)
match_example((0, 0))
match_example((0, 30))
match_example((3, 0))
match_example((5.3, 5))
match_example((5.3, 5, 12.678))

