import numpy as np
import matplotlib.pyplot as plt


def read_as_np_array(filename, limit=10000):
    values = []
    with open(filename, 'rb') as f:
        for line in f:
            if limit == 0:
                break
            limit -= 1
            line = line.decode('utf-8').strip()
            values.append(float(line))

    return np.array(values, dtype=np.float)

if __name__ == '__main__':

    ain0_atrest   = read_as_np_array('data_ain0_atrest.csv')
    ain0_forward  = read_as_np_array('data_ain0_forward.csv')
    ain0_backward = read_as_np_array('data_ain0_backward.csv')

    plt.figure(1)

    plt.subplot(311)
    plt.plot(ain0_atrest)
    plt.title('AIN0 at rest')
    plt.ylim([0, 4096])

    plt.subplot(312)
    plt.plot(ain0_forward)
    plt.title('AIN0 running forward')
    plt.ylim([0, 4096])

    plt.subplot(313)
    plt.plot(ain0_backward)
    plt.title('AIN0 running backward')
    plt.ylim([0, 4096])

    plt.subplots_adjust(hspace=0.5)

    ain2_atrest   = read_as_np_array('data_ain2_atrest.csv')
    ain2_forward  = read_as_np_array('data_ain2_forward.csv')
    ain2_backward = read_as_np_array('data_ain2_backward.csv')

    plt.figure(2)

    plt.subplot(311)
    plt.plot(ain2_atrest)
    plt.title('AIN2 at rest')
    plt.ylim([0, 4096])

    plt.subplot(312)
    plt.plot(ain2_forward)
    plt.title('AIN2 running forward')
    plt.ylim([0, 4096])

    plt.subplot(313)
    plt.plot(ain2_backward)
    plt.title('AIN2 running backward')
    plt.ylim([0, 4096])

    plt.subplots_adjust(hspace=0.5)

    plt.show()
