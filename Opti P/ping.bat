cd C:\Windows\system32\

for /l %%i in (1, 1, 1000) do (
    ping 192.168.1.81
    sleep 1
)
