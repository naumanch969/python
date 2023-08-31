import matplotlib.pyplot as plt

# x5 = [5,6,5,6,5]
# y5 = [5,6,6,5,5]
# x6 = [5,6,5,6,5]
# y6 = [5,6,6,5,5]
# plt.plot(x5,y5,label = 'Line 5')
# plt.plot(x6,y6,label='Line 6',color='green',linestyle='dashed',linewidth=5,marker='o',markerfacecolor='blue',markersize=5)
# plt.ylim(5,6)
# plt.xlim(5,6)   
# plt.legend()


left = [5,5,6,5,6,5]
height = [5,6,6,5,6,5]
tick_label = ['one','two','three','four','five','six']
plt.bar(left,height, tick_label = tick_label, width=.6, color=['blue','orange'])

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Demo Graph - Customization')
 
plt.show()