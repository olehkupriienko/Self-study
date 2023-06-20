files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG',  'solution.Py', 'stepik.org', 'kotlin.ko',
         'github.git', 'ZeBrA.PnG']

result = {i.lower() for i in files if i.lower().endswith('.png')}

print(*sorted(result))
