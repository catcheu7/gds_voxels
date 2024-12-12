import gdspy
import matplotlib.pyplot as plt


def gds_test_plot():
    test = gdspy.GdsLibrary(infile = 'gds_files/Test_GDS_for_GISAXS.gds')
    print(test)
    cell = test.top_level()[0]
    polys = cell.get_polygons(by_spec = True)
    bound = cell.get_bounding_box()
    diff = bound[:,None] - bound[None,:]
    diff[0][1][1]*diff[0][1][0]
    plt.clf()
    plt.ioff()

    fig = plt.figure(figsize = (diff[1][0][0]/100,diff[1][0][1]/100),frameon = False)
    ax = fig.add_subplot()
    plt.axis('off')
    plt.xlim(bound[0][0],bound[1][0])
    plt.ylim(bound[0][1],bound[1][1])
    plt.show()
    
def saxs():
    print("saxs")
    return 1

if __name__=="__main__":
    gds_test_plot()
