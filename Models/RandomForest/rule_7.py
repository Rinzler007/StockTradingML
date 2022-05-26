def findDecision(obj):
   # Feature: RSI, Instances: 115, Entropy: 0.9956
   if obj[1] == 'Hold':
      # Feature: SMA2, Instances: 98, Entropy: 0.9892
      if obj[5] == 'Sell':
         # Feature: SMA1, Instances: 51, Entropy: 0.8974
         if obj[4] == 'Sell':
            # Feature: BB, Instances: 27, Entropy: 0.9911
            if obj[3] == 'Sell':
               # Feature: Closing, Instances: 25, Entropy: 0.971
               if obj[0]>6.207999999999998:
                  # Feature: MACD, Instances: 20, Entropy: 0.9928
                  if obj[2] == 'Buy':
                     return 'No'
                  elif obj[2] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[0]<=6.207999999999998:
                  # Feature: MACD, Instances: 5, Entropy: 0.7219
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[3] == 'Hold':
               return 'Yes'
            else:
               return 'Yes'
         elif obj[4] == 'Buy':
            # Feature: BB, Instances: 24, Entropy: 0.65
            if obj[3] == 'Sell':
               # Feature: MACD, Instances: 22, Entropy: 0.5746
               if obj[2] == 'Sell':
                  # Feature: Closing, Instances: 15, Entropy: 0.7219
                  if obj[0]<=6.207999999999998:
                     return 'No'
                  elif obj[0]>6.207999999999998:
                     return 'No'
                  else:
                     return 'No'
               elif obj[2] == 'Buy':
                  return 'No'
               else:
                  return 'No'
            elif obj[3] == 'Hold':
               # Feature: Closing, Instances: 2, Entropy: 1.0
               if obj[0]>6.207999999999998:
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
            return 'No'
      elif obj[5] == 'Buy':
         # Feature: SMA1, Instances: 47, Entropy: 0.9839
         if obj[4] == 'Buy':
            # Feature: Closing, Instances: 36, Entropy: 0.9436
            if obj[0]>6.207999999999998:
               # Feature: BB, Instances: 31, Entropy: 0.8691
               if obj[3] == 'Hold':
                  # Feature: MACD, Instances: 16, Entropy: 0.6962
                  if obj[2] == 'Buy':
                     return 'Yes'
                  elif obj[2] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[3] == 'Sell':
                  # Feature: MACD, Instances: 15, Entropy: 0.971
                  if obj[2] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[0]<=6.207999999999998:
               # Feature: BB, Instances: 5, Entropy: 0.7219
               if obj[3] == 'Sell':
                  return 'No'
               elif obj[3] == 'Hold':
                  # Feature: MACD, Instances: 2, Entropy: 1.0
                  if obj[2] == 'Sell':
                     return 'Yes'
                  elif obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         elif obj[4] == 'Sell':
            # Feature: BB, Instances: 11, Entropy: 0.9457
            if obj[3] == 'Hold':
               # Feature: Closing, Instances: 6, Entropy: 0.65
               if obj[0]>6.207999999999998:
                  return 'No'
               elif obj[0]<=6.207999999999998:
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[3] == 'Sell':
               # Feature: MACD, Instances: 5, Entropy: 0.971
               if obj[2] == 'Sell':
                  # Feature: Closing, Instances: 3, Entropy: 0.9183
                  if obj[0]>6.207999999999998:
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Buy':
                  # Feature: Closing, Instances: 2, Entropy: 1.0
                  if obj[0]>6.207999999999998:
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'Yes'
         else:
            return 'No'
      else:
         return 'Yes'
   elif obj[1] == 'Sell':
      # Feature: SMA1, Instances: 11, Entropy: 0.4395
      if obj[4] == 'Sell':
         # Feature: SMA2, Instances: 6, Entropy: 0.65
         if obj[5] == 'Sell':
            return 'Yes'
         elif obj[5] == 'Buy':
            # Feature: Closing, Instances: 3, Entropy: 0.9183
            if obj[0]>6.207999999999998:
               # Feature: MACD, Instances: 3, Entropy: 0.9183
               if obj[2] == 'Buy':
                  # Feature: BB, Instances: 3, Entropy: 0.9183
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
      elif obj[4] == 'Buy':
         return 'Yes'
      else:
         return 'Yes'
   elif obj[1] == 'Buy':
      return 'No'
   else:
      return 'No'
