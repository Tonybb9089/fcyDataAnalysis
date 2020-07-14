import pandas as pd
import matplotlib.pyplot as plt
import argumentparser as argumentparser
import matplotlib.dates as mdates
args = argumentparser.ArgumentParser()

from datetime import datetime
time_begin = args.begin
time_end = args.end
item = args.item
readFilename = args.readFile
writeLocation = args.writeFile


if __name__ == '__main__':
    df = pd.read_csv(readFilename)
    df['time'] = pd.to_datetime(df['time'],format='%b-%d %H:%M:%S')
    data = df[(df['time']>=pd.to_datetime(time_begin,format='%b-%d %H:%M:%S')) & (df['time']<=pd.to_datetime(time_end,format='%b-%d %H:%M:%S'))]
    data = data.set_index('time')
    time_index = data.index
    data_time_translation = [str(datetime.strptime(str(d), '%Y-%m-%d %H:%M:%S').time()) for d in time_index]
    y_data = data[item].values
    plt.title(item, size=20)
    xticks = list(range(0, len(data_time_translation), int(len(data_time_translation)/10)))
    plt.gcf().autofmt_xdate()
    plt.xticks(xticks)
    plt.plot(data_time_translation, data[item],'b',lw=2.5)
    plt.savefig(writeLocation)

