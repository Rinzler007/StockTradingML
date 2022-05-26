def findDecision(obj):
   # Feature: BB, Instances: 115, Entropy: 0.9877
   if obj[3] == 'Sell':
      # Feature: MACD, Instances: 63, Entropy: 0.8412
      if obj[2] == 'Sell':
         # Feature: Closing, Instances: 39, Entropy: 0.679
         if obj[0]<=86.040001:
            # Feature: RSI, Instances: 33, Entropy: 0.5328
            if obj[1] == 'Hold':
               # Feature: SMA2, Instances: 30, Entropy: 0.5665
               if obj[5] == 'Buy':
                  # Feature: SMA1, Instances: 17, Entropy: 0.6723
                  if obj[4] == 'Buy':
                     return 'No'
                  elif obj[4] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[5] == 'Sell':
                  # Feature: SMA1, Instances: 13, Entropy: 0.3912
                  if obj[4] == 'Buy':
                     return 'No'
                  elif obj[4] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[1] == 'Buy':
               return 'No'
            else:
               return 'No'
         elif obj[0]>86.040001:
            # Feature: SMA1, Instances: 6, Entropy: 1.0
            if obj[4] == 'Buy':
               # Feature: RSI, Instances: 4, Entropy: 1.0
               if obj[1] == 'Hold':
                  # Feature: SMA2, Instances: 4, Entropy: 1.0
                  if obj[5] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[4] == 'Sell':
               # Feature: RSI, Instances: 2, Entropy: 1.0
               if obj[1] == 'Hold':
                  # Feature: SMA2, Instances: 2, Entropy: 1.0
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
      elif obj[2] == 'Buy':
         # Feature: SMA1, Instances: 24, Entropy: 0.9799
         if obj[4] == 'Sell':
            # Feature: SMA2, Instances: 14, Entropy: 0.9852
            if obj[5] == 'Sell':
               # Feature: Closing, Instances: 12, Entropy: 0.9183
               if obj[0]<=86.040001:
                  # Feature: RSI, Instances: 10, Entropy: 0.971
                  if obj[1] == 'Hold':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[0]>86.040001:
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[5] == 'Buy':
               return 'No'
            else:
               return 'No'
         elif obj[4] == 'Buy':
            # Feature: Closing, Instances: 10, Entropy: 0.7219
            if obj[0]<=86.040001:
               # Feature: RSI, Instances: 6, Entropy: 0.65
               if obj[1] == 'Hold':
                  # Feature: SMA2, Instances: 6, Entropy: 0.65
                  if obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[0]>86.040001:
               # Feature: RSI, Instances: 4, Entropy: 0.8113
               if obj[1] == 'Hold':
                  # Feature: SMA2, Instances: 4, Entropy: 0.8113
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
      else:
         return 'No'
   elif obj[3] == 'Hold':
      # Feature: SMA1, Instances: 41, Entropy: 0.7121
      if obj[4] == 'Buy':
         # Feature: RSI, Instances: 26, Entropy: 0.3912
         if obj[1] == 'Hold':
            # Feature: Closing, Instances: 15, Entropy: 0.5665
            if obj[0]<=86.040001:
               # Feature: MACD, Instances: 9, Entropy: 0.5033
               if obj[2] == 'Buy':
                  return 'Yes'
               elif obj[2] == 'Sell':
                  # Feature: SMA2, Instances: 4, Entropy: 0.8113
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[0]>86.040001:
               # Feature: MACD, Instances: 6, Entropy: 0.65
               if obj[2] == 'Sell':
                  return 'Yes'
               elif obj[2] == 'Buy':
                  # Feature: SMA2, Instances: 3, Entropy: 0.9183
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         elif obj[1] == 'Sell':
            return 'Yes'
         else:
            return 'Yes'
      elif obj[4] == 'Sell':
         # Feature: SMA2, Instances: 15, Entropy: 0.971
         if obj[5] == 'Buy':
            # Feature: Closing, Instances: 8, Entropy: 0.9544
            if obj[0]<=86.040001:
               # Feature: RSI, Instances: 7, Entropy: 0.8631
               if obj[1] == 'Sell':
                  # Feature: MACD, Instances: 4, Entropy: 0.8113
                  if obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[1] == 'Hold':
                  # Feature: MACD, Instances: 3, Entropy: 0.9183
                  if obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[0]>86.040001:
               return 'Yes'
            else:
               return 'Yes'
         elif obj[5] == 'Sell':
            # Feature: Closing, Instances: 7, Entropy: 0.5917
            if obj[0]<=86.040001:
               # Feature: RSI, Instances: 6, Entropy: 0.65
               if obj[1] == 'Hold':
                  # Feature: MACD, Instances: 5, Entropy: 0.7219
                  if obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[1] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[0]>86.040001:
               return 'Yes'
            else:
               return 'Yes'
         else:
            return 'Yes'
      else:
         return 'Yes'
   elif obj[3] == 'Buy':
      return 'No'
   else:
      return 'No'
