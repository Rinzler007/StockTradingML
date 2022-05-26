def findDecision(obj):
   # Feature: RSI, Instances: 2863, Entropy: 0.9989
   if obj[1] == 'Hold':
      # Feature: Closing, Instances: 2339, Entropy: 0.999
      if obj[0]>4.5680000000000005:
         # Feature: BB, Instances: 2330, Entropy: 0.9992
         if obj[3] == 'Sell':
            # Feature: SMA2, Instances: 1623, Entropy: 0.9664
            if obj[5] == 'Sell':
               # Feature: SMA1, Instances: 888, Entropy: 0.927
               if obj[4] == 'Sell':
                  # Feature: MACD, Instances: 502, Entropy: 0.9767
                  if obj[2] == 'Buy':
                     return 'No'
                  elif obj[2] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Buy':
                  # Feature: MACD, Instances: 386, Entropy: 0.8174
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[5] == 'Buy':
               # Feature: SMA1, Instances: 735, Entropy: 0.9936
               if obj[4] == 'Buy':
                  # Feature: MACD, Instances: 541, Entropy: 0.9962
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[4] == 'Sell':
                  # Feature: MACD, Instances: 194, Entropy: 0.9827
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         elif obj[3] == 'Hold':
            # Feature: SMA1, Instances: 637, Entropy: 0.8056
            if obj[4] == 'Buy':
               # Feature: SMA2, Instances: 417, Entropy: 0.7053
               if obj[5] == 'Buy':
                  # Feature: MACD, Instances: 395, Entropy: 0.651
                  if obj[2] == 'Buy':
                     return 'Yes'
                  elif obj[2] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[5] == 'Sell':
                  # Feature: MACD, Instances: 22, Entropy: 0.9457
                  if obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[4] == 'Sell':
               # Feature: MACD, Instances: 220, Entropy: 0.9341
               if obj[2] == 'Buy':
                  # Feature: SMA2, Instances: 218, Entropy: 0.9328
                  if obj[5] == 'Buy':
                     return 'Yes'
                  elif obj[5] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Sell':
                  # Feature: SMA2, Instances: 2, Entropy: 1.0
                  if obj[5] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'Yes'
         elif obj[3] == 'Buy':
            # Feature: MACD, Instances: 70, Entropy: 0.5917
            if obj[2] == 'Sell':
               # Feature: SMA1, Instances: 66, Entropy: 0.5328
               if obj[4] == 'Sell':
                  # Feature: SMA2, Instances: 57, Entropy: 0.5852
                  if obj[5] == 'Sell':
                     return 'No'
                  elif obj[5] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Buy':
                  return 'No'
               else:
                  return 'No'
            elif obj[2] == 'Buy':
               # Feature: SMA1, Instances: 4, Entropy: 1.0
               if obj[4] == 'Sell':
                  # Feature: SMA2, Instances: 4, Entropy: 1.0
                  if obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         else:
            return 'No'
      elif obj[0]<=4.5680000000000005:
         return 'No'
      else:
         return 'No'
   elif obj[1] == 'Sell':
      # Feature: SMA2, Instances: 386, Entropy: 0.3848
      if obj[5] == 'Buy':
         # Feature: SMA1, Instances: 347, Entropy: 0.2943
         if obj[4] == 'Buy':
            # Feature: MACD, Instances: 276, Entropy: 0.1511
            if obj[2] == 'Buy':
               # Feature: Closing, Instances: 266, Entropy: 0.1556
               if obj[0]>4.5680000000000005:
                  # Feature: BB, Instances: 266, Entropy: 0.1556
                  if obj[3] == 'Hold':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[2] == 'Sell':
               return 'Yes'
            else:
               return 'Yes'
         elif obj[4] == 'Sell':
            # Feature: Closing, Instances: 71, Entropy: 0.6554
            if obj[0]>4.5680000000000005:
               # Feature: MACD, Instances: 71, Entropy: 0.6554
               if obj[2] == 'Buy':
                  # Feature: BB, Instances: 71, Entropy: 0.6554
                  if obj[3] == 'Hold':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         else:
            return 'Yes'
      elif obj[5] == 'Sell':
         # Feature: SMA1, Instances: 39, Entropy: 0.8582
         if obj[4] == 'Sell':
            # Feature: BB, Instances: 26, Entropy: 0.8404
            if obj[3] == 'Hold':
               # Feature: Closing, Instances: 24, Entropy: 0.8709
               if obj[0]>4.5680000000000005:
                  # Feature: MACD, Instances: 24, Entropy: 0.8709
                  if obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[3] == 'Sell':
               return 'Yes'
            else:
               return 'Yes'
         elif obj[4] == 'Buy':
            # Feature: BB, Instances: 13, Entropy: 0.8905
            if obj[3] == 'Hold':
               # Feature: Closing, Instances: 11, Entropy: 0.8454
               if obj[0]>4.5680000000000005:
                  # Feature: MACD, Instances: 11, Entropy: 0.8454
                  if obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[3] == 'Sell':
               # Feature: Closing, Instances: 2, Entropy: 1.0
               if obj[0]>4.5680000000000005:
                  # Feature: MACD, Instances: 2, Entropy: 1.0
                  if obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         else:
            return 'Yes'
      else:
         return 'Yes'
   elif obj[1] == 'Buy':
      # Feature: SMA2, Instances: 138, Entropy: 0.1511
      if obj[5] == 'Sell':
         # Feature: Closing, Instances: 108, Entropy: 0.1831
         if obj[0]>4.5680000000000005:
            # Feature: SMA1, Instances: 104, Entropy: 0.1886
            if obj[4] == 'Sell':
               # Feature: BB, Instances: 52, Entropy: 0.2352
               if obj[3] == 'Buy':
                  # Feature: MACD, Instances: 44, Entropy: 0.2668
                  if obj[2] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[3] == 'Sell':
                  return 'No'
               else:
                  return 'No'
            elif obj[4] == 'Buy':
               # Feature: BB, Instances: 52, Entropy: 0.1371
               if obj[3] == 'Sell':
                  # Feature: MACD, Instances: 40, Entropy: 0.1687
                  if obj[2] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[3] == 'Buy':
                  return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         elif obj[0]<=4.5680000000000005:
            return 'No'
         else:
            return 'No'
      elif obj[5] == 'Buy':
         return 'No'
      else:
         return 'No'
   else:
      return 'No'
