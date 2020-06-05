from OpenGL import GL
import glfw

def main():
    if not glfw.init():
        return
    window = glfw.create_window(500,500,"Window in Python",None,None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    while glfw.window_should_close(window) != True:
        glfw.poll_events()
        glfw.swap_buffers(window)

    glfw.terminate()



if __name__ == "__main__":
    main()