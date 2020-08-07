# Python program to test internet speed through speedtest.net

import speedtest

def log(string):
    with open('./Speedtest.txt', 'a') as f:
        f.write(string + '\n')

def start():
    log('||---------------------------------------------||')
    log('Test: '+ input("Name of test: ") + '\n')

def end():
    log('||--------------------NOTES------------------------||\n\n\n')

def downTest():
    try:
        resultTemp = st.download()
        log('Download: ' + str(round(resultTemp/1000000, 2)) + ' Mbps')
        return
    except:
        log("Download test failed")

def upTest():
    try:
        resultTemp = st.upload()
        log('Upload: ' + str(round(resultTemp/1000000, 2)) + ' Mbps')
        return
    except:
        log("Upload test failed")

start()

try:
    st = speedtest.Speedtest()
    print("Running three tests")
    print('')
    print('||---------------------------------------------||')


    for i in range(3):
        print('')
        print('Test #' + str(i+1) + ':')
        log('Test #' + str(i+1) + ':')
        print('Testing download speed...')
        downTest()
        print('Download test completed')
        print('Testing upload speed...')
        upTest()
        print('Upload test completed')
        print('')
        log('')
        print('||---------------------------------------------||')
    end()
except:
    log('No internet!! Test Failed')
