
public static String removeFileExtension(String filename) {
    if (filename.contains(".")) {
        filename = filename.substring(0, filename.lastIndexOf("."));
    }
    return filename;
}

public static int adjustAlpha(int color, float factor) {
    int alpha = Math.round(Color.alpha(color) * factor);
    int red = Color.red(color);
    int green = Color.green(color);
    int blue = Color.blue(color);
    return Color.argb(alpha, red, green, blue);
}
