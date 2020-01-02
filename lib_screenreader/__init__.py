import time

def screen_reader(wx, interval:int=0):
    if interval==0:  # default means only one screenshot
        screen = wx.ScreenDC()
        size = screen.GetSize()
        bmp = wx.EmptyBitmap(size[0], size[1])
        mem = wx.MemoryDC(bmp)
        mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
        del mem  # Release bitmap
        bmp.SaveFile('screenshot.png', wx.BITMAP_TYPE_PNG)
    else:
        i = 0
        while True:  # never end
            time.sleep(interval)  # sleep for `interval` seconds
            screen = wx.ScreenDC()
            size = screen.GetSize()
            bmp = wx.EmptyBitmap(size[0], size[1])
            mem = wx.MemoryDC(bmp)
            mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
            del mem  # Release bitmap
            bmp.SaveFile(f'shots/screenshot{str(i)}.png', wx.BITMAP_TYPE_PNG)
            print(f"[!] Screenshot No. {str(i)} Taken")
            i += 1
