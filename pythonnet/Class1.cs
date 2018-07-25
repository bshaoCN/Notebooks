using System;

namespace ClassLibrary1
{
    public class Class1
    {
        public double Add(double x, double y)
        {
            // exception test
            if (x < 0) throw new Exception("x<0");
            return x + y;
        }
    }
}
