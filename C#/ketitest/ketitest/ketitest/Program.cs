using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ketitest
{
    class Program
    {
        static void Main(string[] args)
        {
            byte[] Data = new byte[] { 0xff, 0x00, 0x00, 0x00 };
            Data = random_bit0to1(Data);

            uint dd = BitConverter.ToUInt32(Data, 0);

            Console.WriteLine(dd);

            Console.ReadKey();
        }

        static byte[] bitAllSet(byte[] origin, bool value)
        {
            byte[] res = (byte[])origin.Clone();
            BitArray bit = new BitArray(res);
            bit.SetAll(value);
            bit.CopyTo(res, 0);
            return res;
        }

        static byte[] random_bit1to0(byte[] origin)
        {
            byte[] res = (byte[])origin.Clone();
            BitArray bit = new BitArray(res);
            int[] idx = GenRandomIndex(bit.Length);
            for (int j = 0; j < bit.Length; j++)
            {
                if (bit.Get(idx[j]) == true)
                {
                    bit.Set(idx[j], false);
                    break;
                }
            }
            bit.CopyTo(res, 0);
            return res;
        }

        static int[] GenRandomIndex(int length)
        {
            int[] index = new int[length];
            for (int i = 0; i < length; i++)
                index[i] = i;
            Random ran = new Random();
            int[] res = new int[length];
            for (int i = 0; i < length; i++)
            {
                int hit = ran.Next(0, length - i - 1);
                res[i] = index[hit];
                int temp = index[length - i - 1];
                index[length - i - 1] = index[hit];
                index[hit] = temp;
            }
            return res;
        }

        static byte[] random_bit0to1(byte[] origin)
        {
            byte[] res = (byte[])origin.Clone();
            BitArray bit = new BitArray(res);
            int[] idx = GenRandomIndex(bit.Length);
            for (int j = 0; j < bit.Length; j++)
            {
                if (bit.Get(idx[j]) == false)
                {
                    bit.Set(idx[j], true);
                    break;
                }
            }
            bit.CopyTo(res, 0);
            return res;
        }


        public static byte[] New_Random_Data(string datatype, string max, string min)
        {
            Random ran = new Random();
            byte[] buf_long = new byte[8];
            switch (datatype.ToUpper())
            {
                case "BOOL":
                    return BitConverter.GetBytes(ran.Next(int.Parse(min), int.Parse(max))>0?true:false);
                case "CHAR":
                case "UCHAR":
                    return BitConverter.GetBytes((byte)ran.Next(byte.Parse(min), byte.Parse(max)));
                case "UINT16":
                    return BitConverter.GetBytes((ushort)ran.Next(ushort.Parse(min), ushort.Parse(max)));
                case "INT16":
                    return BitConverter.GetBytes((short)ran.Next(short.Parse(min), short.Parse(max)));
                case "UINT32":
                    return BitConverter.GetBytes((uint)ran.Next(uint.Parse(min), uint.Parse(max)));
                case "INT32":
                    return BitConverter.GetBytes(ran.Next(int.Parse(min), int.Parse(max)));
                case "UINT64":
                    ran.NextBytes(buf_long);
                    ulong ulongRand = BitConverter.ToUInt64(buf_long, 0);
                    return BitConverter.GetBytes((ulongRand % (ulong.Parse(max) - ulong.Parse(min))) + ulong.Parse(min));
                case "INT64":
                    ran.NextBytes(buf_long);
                    long longRand = BitConverter.ToInt64(buf_long, 0);
                    return BitConverter.GetBytes((longRand % (long.Parse(max) - long.Parse(min))) + long.Parse(min));
                case "FLOAT":
                    float float_Rand = (float)ran.NextDouble();
                    return BitConverter.GetBytes(float.Parse(min) + float_Rand * (float.Parse(max) - float.Parse(min)));
                case "DOUBLE":
                    double double_Rand = ran.NextDouble();
                    return BitConverter.GetBytes(double.Parse(min) + double_Rand*(double.Parse(max) - double.Parse(min)));
            }
            return null;
        }
    }
}
