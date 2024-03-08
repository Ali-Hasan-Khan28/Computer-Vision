for file in os.listdir(datadir):
    if file.endswith('.jpg'):

        file = os.path.splitext(file)[0]
        
        # read in images
        img = cv2.imread('C:/Users/hp/OneDrive/Desktop/5thS/6th Semester Courses/Computer Vision/CV Assignment 1/Computer-Vision/Assigment01/data/img05.jpg')
        # img = cv2.imread('%s/%s.jpg' % (datadir, file))
        
        if (img.ndim == 3):
            img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        img = np.float32(img) / 255
        # actual Hough line code function calls
        img_edge = myEdgeFilter(img, sigma)
        img_threshold = np.float32(img_edge > threshold)
        [img_hough, rhoScale, thetaScale] = myHoughTransform(img_threshold, \
                                                             rhoRes, thetaRes)
        [rhos, thetas] = myHoughLines(img_hough, nLines)

        lines = cv2.HoughLinesP(np.uint8(255 * img_threshold), rhoRes, thetaRes, \
                                50, minLineLength = 20, maxLineGap = 5)

        # everything below here just saves the outputs to files
        fname = '%s/%s_01edge.png' % (resultsdir, file)
        cv2.imwrite(fname, 255 * np.sqrt(img_edge / img_edge.max()))
        
        fname = '%s/%s_02threshold.png' % (resultsdir, file)
        cv2.imwrite(fname, 255 * img_threshold)
        
        fname = '%s/%s_03hough.png' % (resultsdir, file)
        cv2.imwrite(fname, 255 * img_hough / img_hough.max())
        
        fname = '%s/%s_04lines.png' % (resultsdir, file)
        img_lines = np.dstack([img,img,img])
        print("sdssdfsdf")
        print("sdssdfsdf")
        print("sdssdfsdf")
        print("sdssdfsdf")
        print("sdssdfsdf")
        # display line results from myHoughLines function in red
        # display line results from myHoughLines function in red
        for k in np.arange(nLines):
            # Convert radians to degrees and then to an integer index
            theta_degrees = int(np.degrees(thetas[k]))

            a = np.cos(thetaScale[theta_degrees])
            b = np.sin(thetaScale[theta_degrees])
    
            x0 = a * rhoScale[rhos[k]]
            y0 = b * rhoScale[rhos[k]]
    
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
    
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
    
            cv2.line(img_lines, (x1, y1), (x2, y2), (0, 0, 255), 1)

        # for k in np.arange(nLines):
        #     theta_index = int(thetas[k])
        #     a = np.cos(thetaScale[thetas[k]])
        #     b = np.sin(thetaScale[thetas[k]])
            
        #     x0 = a*rhoScale[rhos[k]]
        #     y0 = b*rhoScale[rhos[k]]
            
        #     x1 = int(x0 + 1000*(-b))
        #     y1 = int(y0 + 1000*(a))
            
        #     x2 = int(x0 - 1000*(-b))
        #     y2 = int(y0 - 1000*(a))
            
        #     cv2.line(img_lines,(x1,y1),(x2,y2),(0,0,255),1)
        
        # display line segment results from cv2.HoughLinesP in green
        for line in lines:
            coords = line[0]
            cv2.line(img_lines, (coords[0], coords[1]), (coords[2], coords[3]), \
                     (0, 255, 0), 1)

        cv2.imwrite(fname, 255 * img_lines)