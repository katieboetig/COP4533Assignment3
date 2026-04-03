# COP4533Assignment3
Run all tests at once: for i in {1..10} do echo "test$i" time python src/hvlcs.py < tests/test$i.in > tests/test$i.out done

Single Test: time python src/hvlcs.py < tests/example.in > tests/example.out

note: "python3" might need to replace "python" if working on MacOS.